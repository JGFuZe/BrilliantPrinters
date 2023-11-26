import datetime
from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib import messages

from django_project import settings

from .decorators import allowed_users
from .forms import QuestionForm, CreateUserForm, ProfileForm, FileForm
from .models import Question, Respondent, QuestionFile
from django.contrib.auth import logout

# Question list and detail views
class QuestionListView(generic.ListView):
    model = Question

class QuestionDetailView(generic.DetailView):
    model = Question
    

# Homepage
def index(request):
    return render(request, 'BrilliantPrinters_app/index.html')

#---------------------------------------------
#               Account Views
#---------------------------------------------

def registerUser(request):
    registerForm = CreateUserForm()

    if (request.method == 'POST'):
        registerForm = CreateUserForm(request.POST)

        if (registerForm.is_valid()):
            user = registerForm.save()                              # Save form to user variable
            username = registerForm.cleaned_data.get('username')    # Get Username
            group = Group.objects.get(name='regular_user')           # Get group
            user.groups.add(group)                                  # Add User to group
            newRespondent = Respondent.objects.create(user=user)    # Create Respondent
            newRespondent.save()                                    # Save new respondent
            messages.success(request, 'Registration complete for ' + username) # Send success message
             
            # Redirtect to login page
            return redirect('login')
    
    context = {'form':registerForm}
    return render(request, 'registration/register_user.html', context)


#
@login_required(login_url='login')
def logoutUser(request):
    logout(request)

    return render(request, 'registration/logout.html')


#
#
@login_required(login_url='login')
@allowed_users(allowed_roles=['regular_user'])
def profile(request):
    user = request.user    #
    form = ProfileForm(instance=user) #

    if (request.method == 'POST'):
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if (form.is_valid()):
            form.save()

    context = {'form':form}
    return render(request, 'BrilliantPrinters_app/profile.html', context)


#---------------------------------------------
#               Question Views
#---------------------------------------------

@login_required(login_url='login')
@allowed_users(allowed_roles=['regular_user'])
def createQuestion(request):
    questionForm = QuestionForm()
    fileSubmitForm = FileForm()

    user = User.objects.get(id=request.user.id)     # Get current user
    respondent = Respondent.objects.get(user=user)  # Get Respondent object based on matching user object

    if request.method == 'POST':
        questionForm = QuestionForm(request.POST or None)
        fileSubmitForm = FileForm(request.POST or None, request.FILES or None)

        if all([questionForm.is_valid(), fileSubmitForm.is_valid()]):
            question = questionForm.save()      # Save the form
            question.respondent = respondent    # Set the question respondent with respondent object who made the question
            question.save()                     # Save question
           
            file = fileSubmitForm.save()        # Create and save file object
            file.parentQuestion = question      # Set file's parent question
            file.fileRespondent = respondent    # Set files owner
            file.save()                         # Save file
    
        # Redirect back to portfolio details page
        return redirect('question_list')

    context = {'questionForm':questionForm, 'fileSubmitForm':fileSubmitForm}
    return render(request, 'BrilliantPrinters_app/question_form.html', context)

#
#
@login_required(login_url='login')
@allowed_users(allowed_roles=['regular_user'])
def deleteQuestion(request, question_id):

    # Get question object based on its id
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    
    context = {'question':question}
    return render(request, 'BrilliantPrinters_app/delete_question_form.html', context)



#
#@login_required(login_url='login')
#@allowed_users(allowed_roles=['regular_user'])
def updateQuestion(request, question_id):
    # Get question object based on its id
    question = Question.objects.get(id=question_id)


    if request.method == 'POST':
        # Update form with current information
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            # Save the form
            question = form.save()
        
            # Redirect back to portfolio details page
            return redirect('question_detail', question_id)
    else:
        form = QuestionForm(instance=question)
        
    context = {'form':form}
    return render(request, 'BrilliantPrinters_app/question_form.html', context)




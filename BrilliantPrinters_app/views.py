from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib import messages

from .decorators import allowed_users
from .forms import QuestionForm, CreateUserForm, ProfileForm
from .models import Question, Respondent



# Question list and detail views
class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = Question

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
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


@login_required(login_url='login')
def logoutUser(request):
    return redirect('index')


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

#@login_required(login_url='login')
#@allowed_users(allowed_roles=['regular_user'])
def createQuestion(request):
    form = QuestionForm()

    user = User.objects.get(id=request.user.id)
    respondent = Respondent.objects.get(user=user)
    respondent_id = respondent.id

    if request.method == 'POST':

        question_data = request.POST.copy()
        question_data['respondent_id'] = respondent_id

        form = QuestionForm(question_data)
        if form.is_valid():
            question = form.save()  # Save the form
            question.respondent = respondent
            question.save()         # Save question
            print(question.respondent)

            # Redirect back to portfolio details page
            return redirect('question_list')
        
    context = {'form':form}
    return render(request, 'BrilliantPrinters_app/question_form.html', context)

#
#
@login_required(login_url='login')
@allowed_users(allowed_roles=['regular_user'])
def deleteQuestion(request, question_id):

    # Store project object in project variable
    question = Question.objects.get(id=question_id)

    if request.method == 'POST':
        question.delete()
        return redirect('question_list')
    
    context = {'question':question}
    return render(request, 'BrilliantPrinters_app/delete_question_form.html', context)



#
@login_required(login_url='login')
@allowed_users(allowed_roles=['regular_user'])
def updateQuestion(request, question_id):
    # Store project object in project variable
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


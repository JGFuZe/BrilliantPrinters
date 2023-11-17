from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.contrib import messages

from .decorators import allowed_users
from .forms import QuestionForm, UserCreationForm
from .models import Question
from .models import Respondent

# Create your views here.

# Class Views

# Question list and detail views
class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = Question

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Question


# Functions Views

# Homepage
def index(request):
    return render(request, 'BrilliantPrinters_app/index.html')

#
# Account Views
#


def registerUser(request):

    registerForm = UserCreationForm()

    if (request.method == 'POST'):
        registerForm = UserCreationForm(request.POST)

        if (registerForm.is_valid()):
            user = registerForm.save()                              # Save form to user variable
            username = registerForm.cleaned_data.get('username')    # Get Username
            group = Group.objects.get(name='RegularUser')           # Get group
            newRespondent = Respondent.objects.create(user=user)    # Create Respondent
            newRespondent.groups.add(group)                         # Add Respondent to group
            newRespondent.save()                                    # Save new respondent
            messages.success(request, 'Registration complete for ' + username) # Send success message
             
            # Redirtect to login page
            return redirect('login')
    
    context = {'form':registerForm}
    return render(request, 'registration/register_user.html', context)



# Account Views
@login_required(login_url='login')
def logoutUser(request):
    return redirect('index')














# Question Views

@login_required(login_url='login')
@allowed_users(allowed_roles=['__all__'])
def createQuestion(request):
    form = QuestionForm()

    if request.method == 'POST':
        question_data = request.POST.copy()

        form = QuestionForm(question_data)
        if form.is_valid():
            # Save the form
            question = form.save()

            # Set the projects parent portfolio
            question.save()

            # Redirect back to portfolio details page
            return redirect('question_list')
        
    context = {'form':form}
    return render(request, 'BrilliantPrinters_app/question_form.html', context)

#
#
@login_required(login_url='login')
@allowed_users(allowed_roles=['__all__'])
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
@allowed_users(allowed_roles=['__all__'])
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
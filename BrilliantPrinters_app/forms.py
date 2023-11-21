from django import forms
from django.forms import ModelForm
from .models import Question, TextFile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form

class FileForm(ModelForm):
    file = forms.FileField(widget = forms.TextInput(attrs={
        "name": "images",
        "type": "File",
        "class": "form-control",
        "multiple": "True",
    }), label = "")
    class Meta:
        model = TextFile
        fields = ['file']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields =['title', 'description']


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



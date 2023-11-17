from django.forms import ModelForm
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#create class for project form
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
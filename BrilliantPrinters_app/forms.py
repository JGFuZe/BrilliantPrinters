from django.forms import ModelForm
from .models import Question


#create class for project form
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields =['title']
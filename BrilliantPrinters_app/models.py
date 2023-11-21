from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.




class Respondent(models.Model):
    #replies = models.ForeignKey(QuestionReply, on_delete=models.CASCADE, default=None)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('respondent_detail', args=[str(self.id)])




class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=200, blank=False)
    answered = models.BooleanField(default=False)
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE, null=True)

    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('question_detail', args=[str(self.id)])
    

#WORKING ONN
class QuestionReply(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=200, blank=False)



class TextFile(models.Model):
    file = models.FileField(upload_to='Text_files')
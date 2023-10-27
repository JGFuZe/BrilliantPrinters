from django.db import models
from django.urls import reverse

# Create your models here.



class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False)
    answered = models.BooleanField(default=False)


    #Define default String to return the name for representing the Model object."
    def __str__(self):
        return self.title
    
    #Returns the URL to access a particular instance of MyModelName.
    #if you define this method then Django will automatically
    # add a "View on Site" button to the model's record editing screens in the Admin site
    def get_absolute_url(self):
        return reverse('question_details', args=[str(self.id)])
from django.contrib import admin
from .models import Question, Respondent, QuestionFile



# Register your models here.

admin.site.register(Question)
admin.site.register(Respondent)
admin.site.register(QuestionFile)


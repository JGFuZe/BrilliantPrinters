from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Question

# Create your views here.

# Class Views

# Question list and detail views
class QuestionListView(generic.ListView):
    model = Question

class QuestionDetailView(generic.DetailView):
    model = Question


# Functions Views

# Homepage
def index(request):
    return render(request, 'BrilliantPrinters_app/index.html')
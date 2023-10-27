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

    # override get_context_data to add a project_info object to portfolio_detail.html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_info"] = Question.objects.filter(
            portfolio_id=self.get_object())
        return context



# Functions Views

# Homepage
def index(request):
    return render(request, 'BrilliantPrinters_app/index.html')
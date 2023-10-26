from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic



# Create your views here.

# Homepage
def index(request):
    return render(request, 'BrilliantPrinters_app/index.html')
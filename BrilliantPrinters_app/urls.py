from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('questions', views.QuestionListView.as_view() , name='question_list'),
    path('questions/<int:pk>', views.index, name='question_details'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    path('questions', views.QuestionListView.as_view() , name='question_list'),
    path('questions/<int:pk>', views.QuestionDetailView.as_view() , name='question_detail'),

    path('questions/create_question', views.createQuestion, name='create_question'),
    path('questions/delete_question/<int:question_id>', views.deleteQuestion, name='delete_question'),
]
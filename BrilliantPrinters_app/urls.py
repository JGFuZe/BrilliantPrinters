from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    
    path('questions', views.QuestionListView.as_view() , name='question_list'),
    path('questions/<int:pk>', views.QuestionDetailView.as_view() , name='question_detail'),

    path('questions/create_question', views.createQuestion, name='create_question'),
    path('questions/delete_question/<int:question_id>', views.deleteQuestion, name='delete_question'),
    path('questions/update_question/<int:question_id>', views.updateQuestion, name='update_question'),
    

    # Account Stuff
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', views.registerUser, name='register_user'),
    
    path('profile', views.profile, name='profile'),
    
    #path('accounts/logout', views.logoutUser ,name='logout'),
    #path('accounts/password_change/', name='password_change'),
    #path('accounts/password_change/done', name='password_change_done'),
    #path('accounts/password_reset', name='password_reset'),
    #path('accounts/password_reset/done', name='password_reset_done'),
    #path('accounts/reset/<uidb64>/<token>', name='password_reset_confirm'),
    #path('accounts/reset/done', name='password_reset_confirm'),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
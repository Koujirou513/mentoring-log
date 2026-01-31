from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name='question_list'),
    path('create/', views.QuestionCreateView.as_view(), name='question_create'),
]

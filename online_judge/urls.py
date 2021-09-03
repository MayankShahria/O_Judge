from django.urls import path

from . import views

app_name = 'online_judge'

urlpatterns = [
    path('', views.index, name='index'),
    path('problems/', views.problems, name='problems'),
    path('problems/<str:problem_name>/', views.problem_details, name='problem_details'),
    path('submitted/', views.new_submission, name='new_submission'),
]

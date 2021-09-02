from django.conf.urls import url
from . import views

app_name = 'online_judge'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^problems/$',views.problems,name='problems'),
    url(r'^problems/(?P<problem_name>[a-zA-Z]+)/$', views.problem_details, name='problem_details'),
]

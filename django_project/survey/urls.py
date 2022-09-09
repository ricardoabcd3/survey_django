

from django.urls import path
from . import views
app_name='aplication'
urlpatterns = [
    #ex : /survey/ =home
    path('', views.IndexView.as_view(), name='index'),
    #ex : /survey/5/ = access to object 5 of survey
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    #ex : /survey/5/ = access to object 5 of survey
    path('<int:pk>/resolves/',views.Resolves.as_view(),name='resolves'),
    #ex : /survey/5/ = access to object 5 of survey
    path('vote/<int:question_id>/',views.vote,name='vote'),
    path('questions/',views.AuthorCreateView.as_view(),name='questions'),
    path('answers/',views.ChoiceAnswer.as_view(),name='answers')
    
]

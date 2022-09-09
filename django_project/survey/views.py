
import imp
from secrets import choice
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from survey.models import Question,Choice
from django.urls import reverse
from django.views.generic import CreateView
from django.views import generic
#home

class AuthorCreateView(CreateView):
    model = Question
    fields = ['pub_date','question_text']
class ChoiceAnswer(CreateView):
    model= Choice
    fields=['question','choise_text']
    

class IndexView(generic.ListView):
    template_name='survey/index.html'
    context_object_name='latest_question_list'
    def get_queryset(self):

        #the parameter - means return things in reverse way
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):


    model=Question
    template_name='survey/detail.html'
    
class Resolves(generic.DeleteView):
    
    model=Question
    template_name='survey/vote.html'
# def index(request):
#     latest_question_list=Question.objects.all()
#     return render(request,'survey/index.html',{'latest_question_list':latest_question_list})

# def detail(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)      
#     return render(request,'survey/detail.html',{'question':question})

# def resolves(request,question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'survey/vote.html',{'question':question})

def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        select_choice=question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'survey/detail.html',{
            'question':question,
            'error_message':"no elegiste una respuesta"
        })
    else:
        select_choice.votes +=1
        select_choice.save()
        return HttpResponseRedirect(reverse('aplication:resolves',args=(question.id,)))

    

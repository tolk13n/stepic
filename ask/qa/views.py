#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question
from .models import Answer

def test(request, *args,**kwargs):
    return HttpResponse('()))-OK')

def question(request, id):
    try:
        q = Question.objects.get(id=id)
    except:
        raise Http404
    try:
#        a = Answer.objects.filter(question_id=id)
        a = q.autor
    except Answer.DoesNotExist:
        a = None
#    a = Question.answer.filter(id=id)
#    return HttpResponse('Question_OK!<br>'+q.title+'\n'+q.text)
    return render(request,'qa/index.html',{'q' : q,'a':a })

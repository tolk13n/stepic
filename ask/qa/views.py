#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.core.paginator import Paginator
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
        a = Answer.objects.filter(question_id=id)
    except Answer.DoesNotExist:
        a = None
#    a = Question.answer.filter(id=id)
#    return HttpResponse('Question_OK!<br>'+q.title+'\n'+q.text)
    return render(request,'qa/index.html',{'q' : q,'a':a })


def new(request):
    q = Question.objects.order_by('addet_at')
    q = q.reverse()
    p = Paginator(q,10)
    try:
        id = int(request.GET.get('page'))
    except:
        id = 1
    try:
        new_q = p.page(id)
    except:
        new_q = p.page(1)
    return render(request,'qa/new.html',{'new_q':new_q} )

def popular(request):
    q = Question.objects.order_by('rating')
    q = q.reverse()
    p = Paginator(q,10)
    try:
        id = int(request.GET.get('page'))
    except:
        id = 1
    try:
        new_q = p.page(id)
    except:
        new_q = p.page(1)
    return render(request,'qa/popular.html',{'new_q':new_q} )


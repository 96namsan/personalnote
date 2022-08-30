from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request,'index.html')


def greeting(request):
    foods=['apple','banana','coconut']
    info={
        'name':'woong'
    }

    context={
        'foods':foods,
        'info':info,
    }
    return render(request,'greeting.html',context)

def dinner(request):
    foods=['짜장면','핫크리스피버거','연어초밥']
    randomlist=foods[random.randrange(0,3)]
    context={
        'foods':foods,
        'randomlist':randomlist,

    }
    return render(request,'dinner.html',context)

def image(request):
    return render(request,'image.html')

from datetime import datetime
def template_language(request):
    menus=['자장면','롯데리아','칼국수','바스버거']
    my_sentence='abcdefghijklmnopqrsafasdfadsfadsf'
    message=['apple','banana','cucumber',',mango']
    empty_list=[]
    datetimenow=datetime.now() # 오늘에 대한 날짜/시각 정보

    context={
        'menus':menus,
        'my_sentence':my_sentence,
        'messages':message,
        'empty_list':empty_list,
        'datetimenow':datetimenow,
    }
    return render(request,'template_language.html',context)


def throw(request):
    return render(request,'throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))
    message=request.GET.get('message')
    context={
        'message':message,
    }
    return render(request, 'catch.html',context)
def hello(request,name,age):
    context={
        'name':name,
        'age':age,

    }
    return render(request,'hello.html',context)
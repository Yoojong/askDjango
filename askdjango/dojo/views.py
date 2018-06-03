from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
# Create your views here.
def post_list1(request):
    name = '공유'
    return HttpResponse('''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되겠습니다.</p>'''.format(name=name)
    )

def post_list2(request) :
    name = '유종'
    return render(request, 'dojo/post_list.html', {'name' : name})

def post_list3(request) :
    message = {
        'message' : "안녕, 장고&파이썬",
        'item' : ['파이썬','장고', 'Celery', 'Azure', 'AWS'],
    }

    return JsonResponse(message, json_dumps_params={'ensure_ascii':False})

def excel_download(request) :
    pass

from django.shortcuts import render
from django import http
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def index(request):
    http_host = request.META['HTTP_HOST']
    host = {'http_host': http_host}
    return render(request, 'index.html', host)

def chat_page(request):
    return render(request, 'chat_page.html')

def api_proxy(request):
    if request.method == "POST":
        user_prompt = request.POST.get('user_prompt')
        response = requests.post('http://192.168.1.86:5110/api/prompt_route', data={'user_prompt': user_prompt})
        return JsonResponse({'response': response.text})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def page1():
    http_host = request.META['HTTP_HOST']
    host = {'http_host': http_host}
    return render(request, 'index.html', host)

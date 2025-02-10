from django.http import HttpResponse
from django.shortcuts import render

def http_response_view(request):
    return HttpResponse("Returned By HttpResponse")

def render_view(request):
    return render(request, 'main/my_template.html')
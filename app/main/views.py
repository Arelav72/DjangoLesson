from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, template_name='main/index.html')


def about(request):
    return render(request, template_name='main/about.html')


def contact(request):
    return render(request, template_name='main/contact.html')

def news(request):
    return render(request, template_name='main/news.html')


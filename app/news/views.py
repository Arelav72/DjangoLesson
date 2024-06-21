from django.shortcuts import render
from .models import News_post


def index(request):
    news = News_post.objects.all()
    return render(request, 'news/new.html', {'news': news})



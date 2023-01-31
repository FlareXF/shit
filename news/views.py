from django.shortcuts import render
from .models import Post

def news(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'news'
    }
    return render(request, 'news/news.html', context=context)


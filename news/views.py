from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

def news(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'news'
    }
    return render(request, 'news/news.html', context=context)


class NewsListView(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/create-post.html'

    def from_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
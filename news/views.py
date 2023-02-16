from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    paginate_by = 2

class UserNewsListView(ListView):
    model = Post
    template_name = 'news/user-posts.html'
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        posts = Post.objects.filter(author=user).order_by('-date_posted')
        return posts


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/create-post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/update-post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/delete-post.html'
    context_object_name = 'post'
    success_url = '/news'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

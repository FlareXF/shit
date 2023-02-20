from django.shortcuts import render, get_object_or_404
from main.models import Sites, UserSite, SiteComment
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from main.forms import SiteCommentCreate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.contrib.auth.models import User

# class SiteDetailNCommentViews(FormMixin, DetailView):
# 	model = Sites
# 	template_name = "main/site.html"
# 	context_object_name = "site"
# 	form = SiteCommentCreate

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['form'] = self.form
# 		return context
# 	def post(self, request, *args, **kwargs):
# 		self.object = self.get_object()
# 		form = self.get_form()
		


class SiteDetailView(LoginRequiredMixin , DetailView):
	model = Sites
	template_name = "main/site.html"
	context_object_name = "site"

	form = SiteCommentCreate
	comments = SiteComment

	def post(self, request, *args, **kwargs):
		form = SiteCommentCreate(request.POST)
		if form.is_valid():
			site = self.get_object()
			form.instance.user = request.user
			form.instance.site = site
			form.save()
			return redirect(f'/site/{site.id}/')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['form'] = self.form
		context['comments'] = self.comments.objects.all().filter(site=self.get_object()).order_by('-date')
		return context


class SiteListView(ListView):
	model = Sites
	template_name = "main/main.html"
	context_object_name = "sites"
	paginate_by = 16





class UserSiteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
	model = UserSite
	template_name = "main/user-site.html"
	context_object_name = "site"

	def test_func(self):
		site = self.get_object()
		if site.owner == self.request.user:
			return True
		else:
			return False

class UserSiteListView(LoginRequiredMixin, ListView):
	model = UserSite
	template_name = "main/user-sites.html"
	context_object_name = "sites"
	paginate_by = 16

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		sites = UserSite.objects.all().filter(owner=user)
		return sites

class UserSiteCreate(LoginRequiredMixin, CreateView):
	model = UserSite
	fields = ["name","url"]
	template_name = "main/create-site.html"
	context_object_name = "site"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class UserSiteUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = UserSite
	fields = ["name", "url"]
	template_name = "main/update-site.html"
	context_object_name = "site"

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		site = self.get_object()
		if self.request.user == site.owner:
			return True
		return False

class UserSiteDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = UserSite
	template_name = "main/delete-site.html"
	context_object_name = "site"

	#def get(self, request):
	#	self.success_url = f'user-site/user/{request.user.username}'

	def test_func(self):
		site = self.get_object()
		self.success_url = f'/user-site/user/{self.request.user}'
		if self.request.user == site.owner:
			return True
		return False








def main(request):
	context = {
		'title' : 'main',
		'sites' : Sites.objects.all(),
	}
	return render(request, 'main/main.html', context=context)

def about(request):
	context = {
		'title' : 'about',
	}
	return render(request, 'main/about.html', context=context)

def help(request):
	context = {
		'title' : 'help',
	}
	return render(request, 'main/help.html', context=context)

def contact(request):
	context = {
		'title' : 'constact',
	}
	return render(request, 'main/contact.html', context=context)
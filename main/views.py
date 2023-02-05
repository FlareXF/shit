from django.shortcuts import render
from .models import Sites
from django.views.generic import DetailView, ListView

class SiteDetailView(DetailView):
	model = Sites
	template_name = "main/site.html"
	context_object_name = "site"

class SiteListView(ListView):
	model = Sites
	template_name = "main/main.html"
	context_object_name = "sites"

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
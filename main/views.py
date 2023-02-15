from django.shortcuts import render
from main.models import Sites
from django.views.generic import DetailView, ListView
from main.forms import SiteCommentCreate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class SiteDetailView(DetailView):
	model = Sites
	template_name = "main/site.html"
	context_object_name = "site"

	form = SiteCommentCreate

	def post(self, request, *args, **kwargs):
		form = SiteCommentCreate(request.POST)
		if form.is_valid():
			site = self.get_object()
			form.instance.user = request.user
			form.instance.site = site
			form.save()
			return redirect(f'site/{self.id}/')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = self.form
		return context


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
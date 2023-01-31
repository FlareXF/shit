from django.shortcuts import render

def main(request):
	context = {
		'title' : 'main',
		'sites' : None,
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
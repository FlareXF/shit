from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('help/', views.about, name='help'),
	path('about/', views.help, name='about'),
	path('contact/', views.contact, name='contact')
]
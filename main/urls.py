from django.urls import path
from . import views

urlpatterns = [
	#path('', views.main, name='main'),
	path('', views.SiteListView.as_view(), name='main'),
	path('site/<int:pk>', views.SiteDetailView.as_view(), name='site'),
	path('help/', views.about, name='help'),
	path('about/', views.help, name='about'),
	path('contact/', views.contact, name='contact')
]
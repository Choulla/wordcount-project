
from django.urls import path
from . import views

urlpatterns = [
	path('mmm',views.homepage,name="home"),
		
	path('counter/',views.count,name="count"),
	path('about/',views.about,name="about"),
]

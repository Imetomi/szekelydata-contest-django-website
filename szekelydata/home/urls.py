from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView

urlpatterns = [path('', views.index, name='index'),
			   url(r'^birth/', views.birth, name='birth'),
			   url(r'^livesin/', views.livesin, name='livesin'),
			   url(r'^plots/', views.plots, name='plots'),
			   ]
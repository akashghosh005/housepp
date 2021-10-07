from django.urls import path
from . import views

urlpatterns = [
    path('', views.homebase,name=""),
    path('home', views.home,name="home"),
    path('home2', views.resultprint,name="home2"),
]
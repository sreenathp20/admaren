from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_stories', views.selectStories, name='selectStories'),
]
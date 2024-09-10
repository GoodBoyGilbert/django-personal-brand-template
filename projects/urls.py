from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
  path("", lambda request: redirect('index', permanent=False)),
  path('index', views.index, name="index"),
  path('resume', views.resume, name="resume"),
  path("projects", views.projects, name="projects"),
  path("contact", views.contact, name="contact"),
]
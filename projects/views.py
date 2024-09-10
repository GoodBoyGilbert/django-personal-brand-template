from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.

def index(request):
  return render(request, "index.html")

def resume(request):
  return render(request, "resume.html")

def projects(request):
  
  all_objects = Project.objects.all()

  return render(request, "projects.html", {"projects": all_objects})

def contact(request):
  return render(request, "contact.html")
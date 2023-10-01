from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def projects(request):
    projects = Project.objects.all()         # All projects
    context = {'projects' : projects}
    return render( request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)  # Single project
    tags = projectObj.tags.all()             # project tags
    reviews = projectObj.review_set.all()
    context = {'project' : projectObj, 'tags' : tags, 'reviews': reviews}
    return render(request, 'projects/single-project.html', context)
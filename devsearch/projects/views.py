from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *
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

def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect ('/')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES ,instance=project)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete.html', {'object': project})

def signupUser(request):
    pass

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate( request, username=username, password=password, email=email)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('loginUser')
        
    userform = RegisterForm()
    context = {'userform' : userform}
    return render(request, 'projects/login.html', context)
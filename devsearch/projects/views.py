from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def projects(request):
    query = request.GET.get('query') if request.GET.get('query') != None else ''
    projects = Project.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
                                      )         # All projects
    context = {'projects' : projects}
    return render( request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)  # Single project
    tags = projectObj.tags.all()             # project tags
    reviews = projectObj.review_set.all()
    project_messages = projectObj.message_set.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            project = projectObj,
            body = request.POST.get('body') 
        )
        return redirect('project', pk=projectObj.id)

    context = {'project' : projectObj, 'tags' : tags, 'reviews': reviews, 'project_messages': project_messages}
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='loginUser')
def createProject(request):
    form = ProjectForm()
    tags = Tag.objects.all()

    if request.method == 'POST':
        tag_names = request.POST.getlist('tag')
        tag, created = Tag.objects.get_or_create(name=tag_names)

        project = Project.objects.create(
            owner = request.user,
            # tags = tag,
            title = request.POST.get('title'),
            description = request.POST.get('description'),
            demo_link = request.POST.get('demo_link'),
            source_code = request.POST.get('source_code'),
            featured_image = request.FILES.get('featured_image'),
        )

        project.tags.set(Tag.objects.filter(name__in=tag_names))
        return redirect('projects')
        
    context = {'form': form, 'tags': tags}
    return render(request, 'projects/project-form.html', context)

@login_required(login_url='loginUser')
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

@login_required(login_url='loginUser')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    return render(request, 'projects/delete.html', {'object': project})

def signupUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('projects')
        else:
            return redirect('signupUser')
    
    context = {'form' : form}
    return render(request, 'projects/signup.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = User.objects.get(username=username)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            return redirect('loginUser')
    return render(request, 'projects/login.html')

def logoutUser(request):
    logout(request)
    return redirect('projects')

@login_required(login_url='loginUser')
def devProfile(request, pk):
    user = User.objects.get(id=pk)
    projects = user.project_set.all()
    skills = user.skills.all()
    context = {'projects': projects, 'user': user, 'skills': skills}

    return render(request, 'projects/profile.html', context)

@login_required(login_url='loginUser')
def updateProfile(request, pk):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES ,instance=user)
        if form.is_valid:
            form.save()
            return redirect('profile', pk=user.id)
        
    context = {'form': form}
    return render(request, 'projects/update-profile.html', context)

def developers(request):
    query = request.GET.get('query') if request.GET.get('query') != None else ''
    developers = User.objects.filter(
        Q(name__icontains=query) |
        Q(username__icontains=query) |
        Q(bio__icontains=query) |
        Q(skills__name__icontains=query)
    )
    developers = list(set(developers))
    context = {'developers': developers}
    return render(request, 'projects/developers.html', context)

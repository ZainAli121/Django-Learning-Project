from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

projectList = [
    {
        'id': '1',
        'title' : 'Portfolio Web',
        'description': 'My personal portfolio website',
        'topRated' : True
    },
    {
        'id': '2',
        'title' : 'Ecommerce Web',
        'description': 'An ecommerce web build for the easy shopping',
        'topRated' : False
    },
    {
        'id': '3',
        'title' : 'Blogging App',
        'description': 'Blog app for posting blogs',
        'topRated' : True
    },
]

def projects(request):
    context = {'projects' : projectList}
    return render( request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = None
    for i in projectList:
        if i['id'] == str(pk):
            projectObject = i
    return render(request, 'projects/single-project.html', {'project' : projectObject})
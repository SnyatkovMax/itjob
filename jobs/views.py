from django.shortcuts import render, redirect


from django.contrib.auth import logout
from django.core.paginator import Paginator

#from .forms import PostForm, PostForm2, PostForm3  !!!!!!!!!!!!!!!!!!!!
#from .models import Job   !!!!!!!!!!!!!!!!!!!!!!!!!!!!

def index(request):
    data = dict()
    return render(request, 'jobs/index.html', context=data)


def create(request):
    data = dict()
    return render(request, 'jobs/create.html', context=data)


def details(request):
    data = dict()
    return render(request, 'jobs/details.html', context=data)


def edit(request):
    data = dict()
    return render(request, 'job/edit.html', context=data)


def delete(request):
    data = dict()
    return render(request, 'job/delete.html', context=data)


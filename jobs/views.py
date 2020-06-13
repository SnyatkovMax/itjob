from django.shortcuts import render, redirect
from .forms import PostForm, PostForm2
from .models import Job
from django.contrib.auth import logout
from django.core.paginator import Paginator


def index(request):
    data = dict()
    #data['user'] = 'admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Jobs'
    all_post = Job.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    return render(request, 'jobs/index.html', context=data)


def create(request):
    data = dict()
    #data['user'] = 'admin'
    data['title'] = 'Add a new job'
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin':
            data['format'] = PostForm()
            return render(request, 'jobs/create.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
        # =======================

    elif request.method == 'POST':
        filled_form = PostForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/jobs')


def details(request, post_id):
    data = dict()
    data['title'] = 'View Job'
    data['post'] = Job.objects.get(id=post_id)
    return render(request, 'jobs/details.html', context=data)


def edit(request, post_id):
    data = dict()
    data['title'] = 'Edit Job'
    post = Job.objects.get(id=post_id)
    # del ... ?
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin':
            data['form'] = PostForm2(instance=post)
            data['post'] = post
            return render(request, 'jobs/edit.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        form2 = PostForm2(request.POST)
        # print('==', form2)
        if form2.is_valid():
            # post.company_logo = form2.cleaned_data['company_logo']
            post.job_name = form2.cleaned_data['job_name']
            post.city = form2.cleaned_data['city']
            post.company = form2.cleaned_data['company']
            post.companyURL = form2.cleaned_data['companyURL']
            post.companyEmail = form2.cleaned_data['companyEmail']
            post.lang = form2.cleaned_data['lang']
            post.job_type = form2.cleaned_data['job_type']
            post.experience = form2.cleaned_data['experience']
            post.salary = form2.cleaned_data['salary']
            post.description = form2.cleaned_data['description']

            # fields = ('job_name', 'city', 'company', 'company_logo', 'companyURL', 'companyEmail', 'lang', 'job_type',
            #           'experience', 'salary', 'description')
            post.save()
        return redirect('/jobs')


def delete(request, post_id):
    data = dict()
    data['title'] = 'Delete Job'
    post = Job.objects.get(id=post_id)
    if request.method == 'GET':
        # Блокировка доступа через адресную строку
        # =======================
        if request.user.username == 'admin':
            data['post'] = post
            return render(request, 'jobs/delete.html', context=data)
        else:
            logout(request)  # Блокировка доступа через адресную строку
            return redirect('/accounts/sign_in')
    elif request.method == 'POST':
        post.delete()
        return redirect('/jobs')

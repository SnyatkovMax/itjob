from django.shortcuts import render, redirect
from jobs.models import Job
from django.core.paginator import Paginator


def index(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Job.objects.all()[::-1]  # в обратном порядке
    data['posts'] = all_post
    paginator = Paginator(all_post, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    # return render(request, 'home/index.html')
    return render(request, 'home/index.html', context=data)


def index2(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Job.objects.all()[::-1]  # в обратном порядке
    data['posts'] = all_post
    paginator = Paginator(all_post, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj
    # return render(request, 'home/index.html')
    return render(request, 'home/index-2.html', context=data)


def job_list(request):
    data = dict()
    # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
    data['title'] = 'Listing'
    all_post = Job.objects.all()
    data['posts'] = all_post
    paginator = Paginator(all_post, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data['page_obj'] = page_obj

    return render(request, 'jobs/job-list.html', context=data)


def job_single(request):
    return render(request, 'jobs/job-single.html')


# def my_company(request):
#     return render(request, 'accounts/my_company.html')
def company_list(request):
    return render(request, 'home/company-list.html')


def company_single(request):
    return render(request, 'home/company-single.html')


def create(request):
    return render(request, 'jobs/create.html')


def about_us(request):
    return render(request, 'home/about-us.html')


def faq(request):
    return render(request, 'home/faq.html')


def pricing(request):
    return render(request, 'home/pricing.html')


def blog(request):
    return render(request, 'blog/blog.html')


def blog_right_sidebar(request):
    return render(request, 'blog/blog-right-sidebar.html')


def blog_single(request):
    return render(request, 'blog/blog-single.html')


def contact(request):
    return render(request, 'home/contact.html')

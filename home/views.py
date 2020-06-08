from django.shortcuts import render, redirect

from django.core.paginator import Paginator

#from goods.models import Post   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def index(request):
    return render(request, 'home/index.html')
# def index2(request):
#     return render(request, 'home/index-2.html')


def job_list(request):
    return render(request, 'jobs/job-list.html')
def job_single(request):
    return render(request, 'jobs/job-single.html')


def company_list(request):
    return render(request, 'home/company-list.html')
def company_single(request):
    return render(request, 'home/company-single.html')
def create_job(request):
    return render(request, 'jobs/create-job.html')


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







# def properties_grid_split(request):
#
#     data = dict()
#     # data['user'] = 'temp_admin'  # Временный админ (до включения авторизации)
#     data['title'] = 'Listing'
#     all_post = Post.objects.all()
#     data['posts'] = all_post
#     paginator = Paginator(all_post, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     data['page_obj'] = page_obj
#
#     return render(request, 'home/properties-grid-split.html', context=data)





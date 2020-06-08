from django.urls import path, re_path
from .views import *


urlpatterns = [

    path('', index),
    path('index', index),


    path('job-list', job_list),
    path('job-single', job_single),


    path('company-list', company_list),
    path('company-single', company_single),
    path('create-job', create_job),


    path('about-us', about_us),
    path('faq', faq),
    path('pricing', pricing),


    path('blog', blog),
    path('blog-right-sidebar', blog_right_sidebar),
    path('blog-single', blog_single),


    path('contact', contact),


]


#path('', index2),
# path('index-2', index2),

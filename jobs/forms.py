from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_name', 'city', 'company', 'company_logo', 'companyURL', 'companyEmail', 'lang', 'job_type',
                  'experience', 'salary', 'description')


class PostForm2(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('job_name', 'city', 'company', 'companyURL', 'companyEmail', 'lang', 'job_type',
                  'experience', 'salary', 'description')

# class PostForm3(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ('job_name', 'city', 'company', 'lang', 'job_type', 'experience')

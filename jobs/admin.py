from django.contrib import admin
from .models import JobType, Experience, City, Lang, Job


@admin.register(JobType)
class JobTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Lang)
class LangAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'job_name', 'id', 'city', 'company', 'company_logo', 'companyURL', 'companyEmail', 'lang', 'job_type',
        'salary', 'experience')

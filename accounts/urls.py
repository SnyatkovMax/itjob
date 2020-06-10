from django.urls import path
from .views import *


urlpatterns = [
    path('sign_in', sign_in),
    path('sign_up', sign_up),
    path('sign_out', sign_out),
    path('profile', profile),
    path('ajax_reg', ajax_reg)

]

#path('my_company', my_company),

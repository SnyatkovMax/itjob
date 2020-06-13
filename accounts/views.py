from django.shortcuts import render, redirect
from hashlib import md5
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse


def sign_up(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Sign up'
        return render(request, 'accounts/sign_up.html', context=data)
    elif request.method == 'POST':
        # Извлечение данных их формы
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # Каскад проверок (валидация) - есть другой в sign_up.js
        if pass1_x != pass2_x:
            data['color_x'] = 'red'
            data['report_x'] = 'Пароли не совпадают!'
        elif pass1_x == "":
            # Остальные проверки...
            pass
        else:
            # Техническая проверка
            data['login'] = login_x
            data['pass1'] = pass1_x
            data['pass2'] = pass2_x
            data['email'] = email_x

            # Добавление прользователя в БД
            user = User.objects.create_user(login_x, email_x, pass1_x)
            user.save()

            # Формирования отчета
            data['title'] = 'Registration Report'
            if user is None:
                data['color_x'] = 'red'
                data['report_x'] = 'В регистрации оказано!'
            else:
                data['color_x'] = 'green'
                data['report_x'] = 'Регистрация успешна'

        return render(request, 'accounts/reports.html', context=data)


def sign_in(request):
    data = dict()
    if request.method == 'GET':
        data['title'] = 'Sign in'
        return render(request, 'accounts/sign_in.html', context=data)
    elif request.method == 'POST':
        # Получение данных
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # Проверка подлиности
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            data['color_x'] = 'red'
            data['report_x'] = 'User is not found'
            data['title'] = 'Authorization Report'
            return render(request, 'accounts/reports.html')
        else:
            login(request, user)
            return redirect('/')


def sign_out(request):
    logout(request)
    return redirect('/index')


def profile(request):
    data = dict()
    data['title'] = 'Profile'
    return render(request, 'accounts/profile.html', context=data)


# def my_company(request):
#     data = dict()
#     data['title'] = 'My Company'
#     return render(request, 'accounts/profile.html', context=data)


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')

    try:
        User.objects.get(username=login_y)
        response['message'] = 'занят'
    except User.DoesNotExist:
        response['message'] = 'свободен'

    # Check will be here
    # responce['message'] = 'AJAX work fine!!!'
    return JsonResponse(response)

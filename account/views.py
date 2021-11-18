from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html', context={
            'page_name': 'Реєстрація',
            'page_app': 'account',
            'page_view': 'register'
        })
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        pass2_x = request.POST.get('pass2')
        email_x = request.POST.get('email')

        # 1 - Валідація данних (на стороні сервера)...

        # 2 - Збереження користувача в базі данних...
        user = User.objects.create_user(login_x, email_x, pass1_x)
        if user is None:
            mess = 'В реєстрації відмовлено!'
            color = 'red'
        else:
            user.save()
            mess = 'Реєстрація успішно завершена!'
            color = 'green'

        # 3 - Вивід звіту...
        return render(request, 'account/report.html', context={
            'page_name': 'Звіт по реєстрації',
            'page_app': 'account',
            'page_view': 'report',
            'mess': mess,
            'color': color
        })


def entry(request):
    if request.method == 'GET':
        return render(request, 'account/entry.html', context={
            'page_name': 'Авторизація',
            'page_app': 'account',
            'page_view': 'entry'
        })
    elif request.method == 'POST':
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 - Перевірка правдивості логіна і пароля...
        user = authenticate(request, username=login_x, password=pass1_x)
        if user is None:
            mess = 'Такого логіна незнайдено!'
            color = 'red'
            return render(request, 'account/report.html', context={
                'page_name': 'Звіт про вхід',
                'page_app': 'account',
                'page_view': 'report',
                'mess': mess,
                'color': color
            })
        else:
            login(request, user)
            return redirect('/')


def sign_out(request):
    logout(request)
    return render(request, 'account/logout.html', context={
        'page_name': 'Вихід',
        'page_app': 'account',
        'page_view': 'sing_out'
    })


def ajax_reg(request):
    response = dict()
    login_y = request.GET.get('login')
    try:
        User.objects.get(username=login_y)
        response['message'] = 'занятий'
    except User.DoesnotExist:
        response['message'] = 'вільний'
    return JsonResponse(response)
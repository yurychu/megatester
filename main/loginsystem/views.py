# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from .forms import LoginForm

from django.views import generic


# Create your views here.

#
# def show_login_bar(request):
#     if request.user.is_authenticated():
#         return HttpResponseRedirect(reverse("cases:index"))
#     else:
#         return render(request, 'loginsystem/index.html')


def login(request):
    args = {}
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("launcher:launch"))
            else:
                args['form'] = LoginForm(request.POST)
                args['error_message'] = "Вы не активный пользователь, обратитесь к администратоу"
                return render(request, 'loginsystem/login_page.html', args)
        else:
            args['form'] = LoginForm(request.POST)
            args['error_message'] = "Не верный логин пользователя или пароль"
            return render(request, 'loginsystem/login_page.html', args)
    else:
        args['form'] = LoginForm()
        return render(request, 'loginsystem/login_page.html', args)



#
# def get_name1(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect(reverse("loginsystem:login"))
#     else:
#         form = LoginForm()
#     return render(request, 'loginsystem/login.html', {'form': form})

#
# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     auth.login(request, user)
#                     return HttpResponseRedirect(reverse("cases:cases"))
#                 else:
#                     return render(request, 'loginsystem/login.html', {"error_message": "Вы не активный пользователь"})
#     else:
#         if not request.user.is_authenticated():
#             return render(request, 'loginsystem/login.html', {"error_message": "Неверное значение имени или пароля"})
#         else:
#             pass
#
# def logout(request):
#     auth.logout(request)

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def enter_system(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            pass
            # пользователь не активен
    else:
        pass
        # ошибка логина


def exit_system(request):
    logout(request)

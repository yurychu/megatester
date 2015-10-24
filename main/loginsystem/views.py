from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

from django.views import generic


# Create your views here.

def get_name(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("base_case:cases"))
    else:
        form = LoginForm()

    return render(request, 'loginsystem/login.html', {'form': form})


def enter_system(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse("base_case:cases"))
        else:
            pass
    else:
        pass



def exit_system(request):
    logout(request)

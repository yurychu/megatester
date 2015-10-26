from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import LoginUsernameForm


class LoginView(FormView):
    template_name = "account/login.html"
    form_class = LoginUsernameForm

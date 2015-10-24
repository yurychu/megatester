# -*- coding: utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(label="Пользователь", max_length=30)

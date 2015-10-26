# -*- coding: utf-8 -*-
from django import forms


class GeneratorForm(forms.Form):
    name = forms.CharField(label="Название плана", max_length=30)
    plan = forms.CharField(label="Описание плана", widget=forms.Textarea)

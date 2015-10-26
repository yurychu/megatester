try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = None

from django import forms

from django.contrib import auth

from .hooks import hookset


class LoginForm(forms.Form):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(render_value=False))
    user = None

    def clean(self):
        if self._errors:
            return
        user = auth.authenticate(**self.user_credentials())
        if user:
            if user.is_active:
                self.user = user
            else:
                raise forms.ValidationError("Этот аккаунт не активный")
        else:
            raise forms.ValidationError(self.authentication_fail_message)
        return self.cleaned_data

    def user_credentials(self):
        return hookset.get_user_credentials(self, self.identifier_field)


class LoginUsernameForm(LoginForm):
    username = forms.CharField(label="Имя пользователя", max_length=30)
    authentication_fail_message = "Неверный пользователь или пароль"
    identifier_field = "username"

    def __init__(self, *args, **kwargs):
        super(LoginUsernameForm, self).__init__(*args, **kwargs)
        field_order = ["username", "password"]
        if not OrderedDict or hasattr(self.fields, "keyOrder"):
            self.fields.keyOrder = field_order
        else:
            self.fields = OrderedDict((k, self.fields[k]) for k in field_order)

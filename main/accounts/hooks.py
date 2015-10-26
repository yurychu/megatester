from django.conf import settings


class AccountDefaultHookSet(object):

    def get_user_credentials(self, form, identifier_field):
        return {
            "username": form.cleaned_data[identifier_field],
            "password": form.cleaned_data["password"]
        }


class HookProxy(object):
    def __getattr__(self, item):
        return getattr(settings.ACCOUNT_HOOKSET, item)


hookset = HookProxy()

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_login_bar, name="show_login_bar"),
    url(r'^login/', views.login, name="login"),
]

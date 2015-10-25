from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_login_bar, name="show_start_page"),
    url(r'^login/', views.login, name="login")
]
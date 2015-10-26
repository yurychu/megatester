from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_start_page, name='show_start_page'),
]

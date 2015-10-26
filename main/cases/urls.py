from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListCasesView.as_view(), name='list_cases'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailCase.as_view(), name='detail_case'),
    url(r'^generator/$', views.show_generator, name='generator'),
    url(r'^generate/$', views.generate, name='generate'),
]

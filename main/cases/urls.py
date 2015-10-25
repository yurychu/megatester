from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CasesView.as_view(), name='cases'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailCase.as_view(), name='detail_case'),
    url(r'^$', views.index, name='index')
]

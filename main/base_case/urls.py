from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cases/$', views.cases, name='cases'),
    url(r'^cases/(?P<case_id>[0-9]+)/$', views.detail_case, name='detail_case')
]

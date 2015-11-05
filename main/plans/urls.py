from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListPlansView.as_view(), name='list_plans'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailPlan.as_view(), name='detail_plan'),
    url(r'^create_plan/$', views.CreatePlan.as_view(), name='create_plan')
]

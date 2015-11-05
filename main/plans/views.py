from django.shortcuts import render
from django.views import generic
from .models import Plans


class ListPlansView(generic.ListView):
    template_name = "plans/index.html"
    context_object_name = "list_plans"

    def get_queryset(self):
        return Plans.objects.all()


class DetailPlan(generic.DetailView):
    model = Plans
    template_name = "plans/detail_plan.html"
    context_object_name = "plan"


class CreatePlan(generic.DetailView):
    pass

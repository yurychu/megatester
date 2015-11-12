from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

from django.views import generic
from .models import Plans
from .forms import CreatePlanForm
from django.utils import timezone


class ListPlansView(generic.ListView):
    template_name = "plans/index.html"
    context_object_name = "list_plans"

    def get_queryset(self):
        return Plans.objects.all()


class DetailPlan(generic.DetailView):
    model = Plans
    template_name = "plans/detail_plan.html"
    context_object_name = "plan"


class CreatePlan(generic.edit.CreateView):
    template_name = 'plans/create_plan.html'
    model = Plans
    success_url = '/'
    fields = [
            'title',
            'stand_url',
            'stand_user',
            'species',
            'process',
            'text',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = timezone.now()
        return super(CreatePlan, self).form_valid(form)


def generate(request, id):
    plan = Plans.objects.get(pk=id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    p = canvas.Canvas(response)

    p.drawString(9*cm, 22*cm, plan.text)

    p.showPage()
    p.save()
    return response

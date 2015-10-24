from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Cases


# Create your views here.

class CasesView(generic.ListView):
    template_name = "base_case/index.html"
    context_object_name = "list_cases"

    def get_queryset(self):
        return Cases.objects.all()


class DetailCase(generic.DetailView):
    model = Cases
    template_name = "base_case/detail_case.html"
    context_object_name = "case"


# def detail_case(request, case_id):
#     case = get_object_or_404(Cases, pk=case_id)
#     return render(request, 'base_case/detail_case.html', {"case": case})

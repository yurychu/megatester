from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Cases
from .forms import GeneratorForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class ListCasesView(generic.ListView):
    template_name = "cases/index.html"
    context_object_name = "list_cases"

    def get_queryset(self):
        return Cases.objects.all()


class DetailCase(generic.DetailView):
    model = Cases
    template_name = "cases/detail_case.html"
    context_object_name = "case"


# def detail_case(request, case_id):
#     case = get_object_or_404(Cases, pk=case_id)
#     return render(request, 'cases/detail_case.html', {"case": case})


def show_generator(request):
    form = GeneratorForm()
    return render(request, 'cases/generator.html', {'form': form})


def generate(request):
    name = request.POST['name']
    plan = request.POST['plan']

    base = Cases(title=name, text=plan, date=timezone.now(), user=request.user)
    base.save()

    arg = {
        "name": name,
        "plan": plan,
    }
    return render(request, 'cases/result.html', arg)

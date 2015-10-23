from django.shortcuts import render, get_object_or_404
from .models import Cases


# Create your views here.


def cases(request):
    list_cases = Cases.objects.all()
    context = {'list_cases': list_cases}
    return render(request, 'base_case/index.html', context)


def detail_case(request, case_id):
    case = get_object_or_404(Cases, pk=case_id)
    return render(request, 'base_case/detail_case.html', {"case": case})

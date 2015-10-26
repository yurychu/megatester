from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.


def show_start_page(request):
    return render(request, 'launcher/index.html')

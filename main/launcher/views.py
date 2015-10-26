from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required()
def show_start_page(request):
    return render(request, 'launcher/index.html')

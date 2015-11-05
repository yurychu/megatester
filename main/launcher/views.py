from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/loginsystem/login/')
def launch(request):
    return render(request, 'launcher/index.html')

from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from django.contrib.auth import login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
def index_template(request):
    sc_app_data = {
    'app': 'Django',
    'num': range(10),
    }
    return render(request, 'index.html', sc_app_data)
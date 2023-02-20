from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Sample,db_select
from .forms import SampleForm
from django.db import connection



#sample 追加####################
def lists(request):
    
    sample_list = Sample.objects.all()
    form = SampleForm(request.POST or None)
    context = {
        'sample_list':sample_list,
        'form':form,
    }
    if request.method == 'POST':
        if form.is_valid():

            # create()の場合
            Sample.objects.create(**form.cleaned_data)

# # save()の場合
#             sample = Sample(**form.cleaned_data)
#             sample.save

            return render(request, 'lists.html', context)
    return render(request, 'lists.html', context)


################################

@login_required
def home(request):
    data = db_select()
    sc_app_data = {
    'app': 'Django',
    'num': range(10),
    'inf': data,
    }
    # context={'db_inf':db_select}
    return render(request, 'home.html', sc_app_data)






def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to='/sc_app/home/')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'login_app/signup.html', param)


def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                    return redirect(to='/sc_app/home/')
                else:
                    return redirect(to=next)
    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'login_app/login.html', param)

def logout_view(request):
    logout(request)

    return render(request, 'login_app/logout.html')

@login_required
def user_view(request):
    user = request.user

    params = {
        'user': user
    }

    return render(request, 'login_app/user.html', params)

@login_required
def other_view(request):
    users = User.objects.exclude(username=request.user.username)

    params = {
        'users': users
    }

    return render(request, 'login_app/other.html', params)
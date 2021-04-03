from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import TecherModel,Timetable
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.

def category(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')



@login_required(login_url='/accounts/login/')
@staff_member_required
def add_data(request):
    if request.method == 'POST':
        form = TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_data')
    else:
        form = TimeTableForm()
    return render(request, 'teacher.html', {
        'form': form
    })

def singup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')
            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = name[0]
            usr.last_name = name[1]
            usr.save()
            return redirect('/')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def detail(request):
    data = Timetable.objects.all()
    return render(request,'student.html',{'data':data})
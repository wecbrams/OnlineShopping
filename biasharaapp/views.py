from enum import member
from django.shortcuts import render, redirect
from biasharaapp.models import Member
from biasharaapp.forms import ProductsForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['password'],
                        email=request.POST['email'],
                        username=request.POST['username'], password=request.POST['password'])

        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            Member.objects.filter(username=request.POST['username'],
                                  password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def add(request):
    if request.method=="POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductsForm()
        return render(request, 'addproduct.html', {'form': form})

from django.shortcuts import render, redirect

from webapp.models import Login, Register


# Create your views here.

def index(request):
    return render(request, 'index.html')

def mans(request):
    return render(request, 'mans_clothes.html')

def contact(request):
    return render(request, 'contact.html')

def woman(request):
    return render(request, 'womans_clothes.html')

def computer(request):
    return render(request, 'computers.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        login = Login(email, password)
        login.save()
        return redirect('index/')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        C_password = request.POST['C_password']

        register = Register(full_name, email, password, C_password)
        register.save()
        return redirect('login/')

    return render(request, 'signup.html')



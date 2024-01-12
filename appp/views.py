from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'base.html')



def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            return render(request, 'login.html') 

    return render(request, 'login.html')



def logout(request):
    logout(request)
    return redirect("/login")
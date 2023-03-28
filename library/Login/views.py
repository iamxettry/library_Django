from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1!=pass2:
            return HttpResponse("your password and confirm password")
        else:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect('login')
    return render(request,"pages/Signup.html")
    
def Login(request):
    error={"error":"Incorrect password !!"}
    if request.method=="POST":
        uname=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,"pages/login.html", error)

    return render(request,"pages/login.html")


def LogoutPage(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def index(request):
    user=request.user
    contex={'user':user}
    return render(request, "index.html",contex)
from django.shortcuts import render, HttpResponse, redirect
from .forms import NewUserForm      # user_name, email, pass1, pass2
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def user_signup(request):
    if request.method == "GET":
        form = NewUserForm()
        return render(request= request, template_name= "register.html", context= {"signup_form" : form})
    elif request.method == "POST":
        data = request.POST
        form = NewUserForm(data)
        if form.is_valid():
            user = form.save()      # User enter in auth_user table
            print(user) 
            messages.success(request, f"User '{user.username}' register successfully... Now you can login here..." )
            return redirect("user_login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            

def user_login(request):
    if request.method == "GET":
        return render(request, "login.html", {"login_form": AuthenticationForm()})
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=u_name, password=password)
            if user is not None:
                login(request, user)        # session mentain karne k liye
                messages.success(request, f"You are logged in successfully as {u_name}.")
                return redirect("home_page")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
            return redirect("user_login")

def user_logout(request):
    logout(request)
    return redirect("user_login")
from django.shortcuts import  render, redirect
from users.forms import (CreateUserForm)
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    template = 'users/register.html'
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect("users:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CreateUserForm()
    
    return render (request, template, context={"register_form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("users:register")
            else:
                messages.error(request,"Invalid username or password.")
                print(form.error_messages)
                return render(request, "users/login.html", context={"login_form":form})
        else:
            messages.error(request,"Invalid username or password.")
            print(form.error_messages)
    form = AuthenticationForm()
    return render(request, "users/login.html", context={"login_form":form})
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    #logging in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Your are logged in")
            return redirect('home')
        else:
            messages.success(request, "Username Passowrd not matching, please try again!")
            return redirect('home')
    else:
        return render(request, 'website/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out.")
    return redirect('home')


def register_user(request):
    if request.method == "POST" :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.success(request, "You have registered succesfully. Welcome!!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html', {'form': form})
    
    return render(request, 'website/register.html', {'form': form})
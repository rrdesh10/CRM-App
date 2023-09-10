from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Record


def home(request):

    records = Record.objects.all()

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
        return render(request, 'website/home.html', {'records':records})


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


def record_detail(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'website/record_detail.html', {'customer_record': customer_record, 'pk':pk})
    else:
        messages.success(request, "Please login to view record detail.")
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted")
        return redirect('home')
    else:
        messages.success(request, "Please login to delete record")
        return redirect('home')
    

def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add = form.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        else:
            return render(request, 'website/record_add.html', {'form': form})
    else:
        messages.success(request, "Please login to add records.")
        return redirect('home')
    

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has be updated")
            return redirect('home')
        return render(request, 'website/record_update.html', {'form': form})
    else:
        messages.success(request, "Please login to update records.")
        return redirect('home')
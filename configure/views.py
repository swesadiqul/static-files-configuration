from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home_view(request):
    if request.method == "GET":
        email = request.GET.get('email')
        password = request.GET.get('password')
        check = request.GET.get('check')
        print(email)
        print(password)
        print(check)
    return render(request, template_name="index.html")


def signUpView(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = Registration(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
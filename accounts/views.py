from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import CustomUser


# Create your views here.
def register(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        role = request.POST['role']

        if password1==password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'This email is already registered')
                return redirect('register')
            else:
                user = CustomUser.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    role=role
                )
                messages.success(request, 'User created successfully!')
                return redirect('login')
        else:
            messages.warning(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password1']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('/')
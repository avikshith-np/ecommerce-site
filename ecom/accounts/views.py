from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def registerview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error_message = 'Passwords do not match.'
            return render(request, 'register.html', {'error_message': error_message})

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            error_message = 'Username is already taken.'
            return render(request, 'register.html', {'error_message': error_message})

        # Create the user account
        user = User.objects.create_user(username=username, password=password1)
        user.save()

        return redirect('login')  

    return render(request, 'register.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log in the user
            login(request, user)
            return redirect('frontpage')
        else:
            # Authentication failed, display an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logoutrequest(request):
    logout(request)
    return redirect('frontpage')
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout

#from .forms import CustomUserCreationForm

class UserRegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log in the user
            login(request, user)
            return redirect('frontpage')  # Replace 'home' with your desired redirect URL after successful login
        else:
            # Authentication failed, display an error message
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def logoutrequest(request):
    logout(request)
    return redirect('frontpage')
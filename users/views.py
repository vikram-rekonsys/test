from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib import messages

from django.urls import reverse_lazy
from .models import User
from .forms import UserForm,UserLoginForm, UserSignupForm

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')  # Redirect to user list page after successful creation

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('user_list')  # Redirect to user list page after successful update

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/user/list')  # Redirect to a success page
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

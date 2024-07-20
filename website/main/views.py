from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import ProblemForm
from django.contrib import messages
from .models import Problem
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    # Fetch problems posted by the logged-in user
    problems = Problem.objects.filter(user=request.user)
    return render(request, 'home.html', {'problems': problems})

@login_required
def submit_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            messages.success(request, 'Problem submitted successfully!')
            return redirect('home')
    else:
        form = ProblemForm()
    return render(request, 'submit_problem.html', {'form': form})


# Note: LogoutView is not explicitly defined here but is used in urls.py
def base(request):
    return render(request, 'base.html')
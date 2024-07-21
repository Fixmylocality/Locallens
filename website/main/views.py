from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from .forms import ProblemForm
from django.contrib import messages
from .models import Problem
from .forms import FundingForm
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404

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
    if request.user.is_authenticated:
        # Change filter to use 'created_by'
        problems = Problem.objects.filter(created_by=request.user)
    else:
        problems = None
    return render(request, 'home.html', {'problems': problems})

@login_required
def submit_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.created_by = request.user  # Assign the logged-in user
            problem.save()
            return redirect('home')  # Redirect to a success page or the home page
    else:
        form = ProblemForm()
    
    return render(request, 'submit_problem.html', {'form': form})


# Note: LogoutView is not explicitly defined here but is used in urls.py
def base(request):
    return render(request, 'base.html')



def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    context = {
        'problem': problem,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'problem_detail.html', context)




def funding_view(request):
    if request.method == 'POST':
        form = FundingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('base')  # Redirect to a success page
    else:
        form = FundingForm()
    return render(request, 'funding.html', {'form': form})

def community(request):
    # Fetch all problems from the database
    problems = Problem.objects.all()
    # Render the community template with the problems context
    return render(request, 'community.html', {'problems': problems})
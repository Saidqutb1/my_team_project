from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, PaintingForm
from .models import Painting


# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('users:welcome')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:welcome')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('users:home')


@login_required
def welcome(request):
    return render(request, 'users/welcome.html', {'username': request.user.username})


@login_required
def upload_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save(commit=False)
            painting.user = request.user
            painting.save()
            return redirect('users:my_paintings')
    else:
        form = PaintingForm()
    return render(request, 'users/upload_painting.html', {'form': form})


@login_required
def my_paintings(request):
    paintings = Painting.objects.filter(user=request.user)
    return render(request, 'users/my_paintings.html', {'paintings': paintings})

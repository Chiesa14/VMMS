from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import User


# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_role = form.cleaned_data.get('user_role')
            if user_role == 'mechanic':
                user.is_staff = True
            else:
                user.is_staff = False

            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url="/auth/login/")
def delete_user(request, user_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to delete users.")

    if request.method == "POST":
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully."})
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)


def logout_user(request):
    logout(request)
    return redirect('login')

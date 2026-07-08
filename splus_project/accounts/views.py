from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    return render(request, 'accounts/register.html')
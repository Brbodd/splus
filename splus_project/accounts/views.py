from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login as auth_login

from .forms import RegisterForm
from .models import User



def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def profile(request):
    return render(request, 'accounts/profile.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()

        context = {
            'register_form': register_form
        }

        return render(
            request,
            'accounts/register.html',
            context
        )

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            phone_number = register_form.cleaned_data['phone_number']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']


            if User.objects.filter(phone_number=phone_number).exists():
                register_form.add_error(
                    'phone_number',
                    'این شماره قبلا وارد شده است.'
                )

            else:

                user = User.objects.create_user(
                    username=phone_number,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                    phone_number=phone_number,
                )

                # ورود خودکار کاربر
                auth_login(request, user)

                return redirect('')

        context = {
            'register_form': register_form
        }

        return render(
            request,
            'accounts/register.html',
            context
        )

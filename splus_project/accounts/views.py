from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login

from .forms import RegisterForm, LoginForm
from .models import User


class ProfileView(View):
    def get(self, request):

        if request.user.is_authenticated:

            user = User.objects.get(id=request.user.id)

            content = {
                'user': user,
            }

            return render(
                request,
                'accounts/profile.html',
                content
            )

        else:

            return redirect('login')


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()

        context = {
            'login_form': login_form
        }

        return render(
            request,
            'accounts/login.html',
            context
        )

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            phone_number = login_form.cleaned_data.get('phone_number')

            try:

                user = User.objects.get(phone_number=phone_number)

            except User.DoesNotExist:

                login_form.add_error(
                    None,
                    'لطفا ابتدا ثبت نام کنید.'
                )

                return render(
                    request,
                    'accounts/login.html',
                    {
                        'login_form': login_form
                    }
                )

            login(request, user)

            return redirect('home')


        context = {
            'login_form': login_form
        }

        return render(
            request,
            'accounts/login.html',
            context
        )


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

                return redirect('home')

        context = {
            'register_form': register_form
        }

        return render(
            request,
            'accounts/register.html',
            context
        )


class LogoutView(View):
    def post(self, request):

        logout(request)

        return redirect('login')
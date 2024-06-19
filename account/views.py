from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from plyer import notification


def login_page(request):
    next_page = request.GET.get('redirect')
    if request.user.is_authenticated:
        return redirect('home:home_page')
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request,  username=username, password=password)
            if user is not None:
                login(request, user)
                notification.notify(
                    title='Successful!!',
                    message=f'Welcome Back {request.user}',
                    timeout=2
                )
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('home:home_page')
            else:
                notification.notify(
                    title='Failed!!',
                    message=f'Invalid',
                    timeout=2
                )
                login_form.add_error('password', 'Invalid username or password')
    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home:home_page')
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            email = register_form.cleaned_data.get('email')
            password2 = register_form.cleaned_data.get('password2')
            user = User.objects.create_user(username=username, password=password2)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            notification.notify(
                title='Successful!!',
                message='for use your account please log in',
                timeout=2
            )
            return redirect('account:login_page')
    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def logout_page(request):
    logout(request)
    notification.notify(
        title='Successful!!',
        message='Goodbye',
        timeout=2
    )
    return redirect('home:home_page')
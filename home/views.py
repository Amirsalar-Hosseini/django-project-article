from django.shortcuts import render
from django.contrib.auth.models import User


def home_page(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'home/index.html', context)

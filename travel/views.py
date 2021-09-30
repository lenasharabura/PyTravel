from django.shortcuts import render


def home(request):
    name = 'Elena'

    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Elena'
    return render(request, 'about.html', {'name': name})
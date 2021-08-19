from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def ai(request):
    return render(request, "ai.html")


def com(request):
    return render(request, "com.html")

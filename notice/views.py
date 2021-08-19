from django.shortcuts import render


def home(request):
    return render(request, "notice/home.html")


def ai(request):
    return render(request, "notice/ai.html")


def com(request):
    return render(request, "notice/com.html")

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from . import models


def home(request):

    ai_posts = models.AiNotice.objects.filter().order_by("-number")[:10]
    com_posts = models.ComNotice.objects.filter().order_by("-number")[:10]

    return render(
        request, "notice/home2.html", {"ai_posts": ai_posts, "com_posts": com_posts}
    )


def ai(request):
    posts = models.AiNotice.objects.filter().order_by("-date")
    paginator = Paginator(posts, 20)
    page_num = request.GET.get("page")
    posts = paginator.get_page(page_num)
    return render(request, "notice/detail.html", {"posts": posts, "name": "AI융합 전공"})


def com(request):
    posts = models.ComNotice.objects.filter().order_by("-date")
    paginator = Paginator(posts, 20)
    page_num = request.GET.get("page")
    posts = paginator.get_page(page_num)
    return render(request, "notice/detail.html", {"posts": posts, "name": "컴퓨터 공학부"})

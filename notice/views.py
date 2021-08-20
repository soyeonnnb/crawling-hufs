from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from . import models


def home(request):

    ai_posts = models.AiNotice.objects.filter().order_by("number")[:10]
    com_posts = models.ComNotice.objects.filter().order_by("number")[:10]

    return render(
        request, "notice/home2.html", {"ai_posts": ai_posts, "com_posts": com_posts}
    )


def ai(request):
    return render(request, "notice/ai.html")


class AiView(ListView):

    """AiView Definition"""

    model = models.AiNotice
    paginate_py = 15
    paginate_orphans = 3
    ordering = "date"
    context_object_name = "ai"


def com(request):
    return render(request, "notice/com.html")

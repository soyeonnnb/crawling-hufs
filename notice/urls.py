from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path("", views.home, name="home"),
    path("ai/", views.ai, name="ai"),
    path("com/", views.com, name="com"),
]

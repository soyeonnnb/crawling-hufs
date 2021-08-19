from django.urls import path
from . import views

app_name = "free"

urlpatterns = [
    path("", views.home, name="home"),
]

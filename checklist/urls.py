from django.urls import path
from . import views

app_name = "checklist"

urlpatterns = [
    path("", views.home, name="home"),
]

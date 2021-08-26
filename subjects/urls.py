from django.urls import path
from . import views

app_name = "subjects"

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.SearchView.as_view(), name="search"),
]

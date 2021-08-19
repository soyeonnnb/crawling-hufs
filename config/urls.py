from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls"), name="core"),
    path("checklist/", include("checklist.urls"), name="checklist"),
    path("free/", include("free.urls"), name="free"),
    path("qanda/", include("q_and_a.urls"), name="qanda"),
    path("users/", include("users.urls"), name="users"),
    path("notice/", include("notice.urls"), name="notice"),
    path("admin/", admin.site.urls),
]

from django.contrib import admin
from . import models


@admin.register(models.AiNotice)
class AiNoticeAdmin(admin.ModelAdmin):

    """AiNotice Admin Definition"""

    list_display = (
        "title",
        "author",
        "date",
        "link",
    )
    ordering = ("-date",)


@admin.register(models.ComNotice)
class ComNoticeAdmin(admin.ModelAdmin):

    """ComNotice Admin Definition"""

    list_display = (
        "title",
        "author",
        "date",
        "link",
    )
    ordering = ("-date",)

from django.contrib import admin
from . import models


@admin.register(models.AiNotice)
class AiNoticeAdmin(admin.ModelAdmin):

    """AiNotice Admin Definition"""

    list_display = ("number", "title", "author", "date", "link", "specific_id")
    ordering = ("-number",)


@admin.register(models.ComNotice)
class ComNoticeAdmin(admin.ModelAdmin):

    """ComNotice Admin Definition"""

    list_display = ("number", "title", "author", "date", "link", "specific_id")
    ordering = ("-number",)

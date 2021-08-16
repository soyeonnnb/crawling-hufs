from django.contrib import admin
from . import models


@admin.register(models.AiData)
class AiCrawlerAdmin(admin.ModelAdmin):

    """AiCrawler Admin Definition"""

    list_display = (
        "title",
        "author",
        "date",
        "link",
    )


@admin.register(models.ComData)
class ComCrawlerAdmin(admin.ModelAdmin):

    """ComCrawler Admin Definition"""

    list_display = (
        "title",
        "author",
        "date",
        "link",
    )

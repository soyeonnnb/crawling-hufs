from django.contrib import admin
from . import models


@admin.register(models.AiData)
class AiCrawlerAdmin(admin.ModelAdmin):

    """AiCrawler Admin Definition"""

    list_display = (
        "title",
        "author",
        "date",
        "text",
        "link",
    )

from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)


@admin.register(models.Subjects)
class SubjectsAdmin(admin.ModelAdmin):

    """Subjects Admin Definition"""

    list_display = (
        "name",
        "require",
        "year",
        "credit",
        "semester",
        "track",
    )

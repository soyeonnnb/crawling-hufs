from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Subject)
class SubjectsAdmin(admin.ModelAdmin):

    """Subjects Admin"""

    list_display = (
        "name",
        "require",
        "year",
        "credit",
        "track",
    )
    list_filter = ("require", "year", "track")


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):

    """Track Admin"""

    list_display = ("name",)

    def __str__(self):
        return self.name

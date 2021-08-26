from django.contrib import admin
from .models import User

# Register your models here.
@admin.site.register(User)
class UserAdmin(admin.ModelAdmin):

    """User Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "email",
                    "nickname",
                    "is_staff",
                    "is_active",
                )
            },
        ),
        ("Times", {"fields": ("date_joined",)}),
        ("Last Details", {"fields": ("subjects",)}),
    )

    list_display = (
        "email",
        "nickname",
        "is_staff",
        "is_active",
    )
    filter_horizontal = "subjects"

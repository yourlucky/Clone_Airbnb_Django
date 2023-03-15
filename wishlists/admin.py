from django.contrib import admin

from .models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    """WishList Admin Definition"""
    list_display=(
        "name",
        "user",
        "created_at",
        "updated_at",
    )

# Register your models here.

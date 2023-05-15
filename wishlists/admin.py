from django.contrib import admin

from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """WishList Admin Definition"""
    list_display=(
        "name",
        "user",
        "created_at",
        "updated_at",
    )

# Register your models here.

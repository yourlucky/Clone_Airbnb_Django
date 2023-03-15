from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenties",
        "owner",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "kind",
        "owner",
        "pet_friendly",
        "amenities",
        "created_at",
        "updated_at",
    )
    def total_amenties(self,room):
        return room.amenities.count()

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_filter=(
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

    



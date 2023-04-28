from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def reset_prices(modeladmin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    action = (reset_prices,)
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenties",
        "owner",
        "rating",
        "created_at",
        "simple_count",
    )
    search_fields = (
        "^name", #^ means startswith
        "=price",#= means exact same 
        "owner__username", #__ means foreign key
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

    



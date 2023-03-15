from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    """ Room Model Definition """
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place","Entire Place",)
        PRIVATE_ROOM = ("private_room","Private Room",)
        SHARED_ROOM = ("shared","Shared Room",)
    
    name = models.CharField(max_length=180,default="")

    country=models.CharField(max_length=50, default="한국",)
    city = models.CharField(max_length=80, default="서울",)
    price = models.PositiveBigIntegerField()
    rooms =models.PositiveBigIntegerField()
    toilets=models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250,)
    pet_friendly = models.BooleanField(default=False,)
    kind = models.CharField(max_length=20,choices=RoomKindChoices.choices,)
    owner = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="rooms",)
    amenities = models.ManyToManyField("rooms.Amenity",related_name="rooms",)
    category = models.ForeignKey("categories.Category",on_delete=models.SET_NULL,null=True,blank=True,)
    created_at= models.DateTimeField(auto_now_add=True,)
    updated_at= models.DateTimeField(auto_now=True,)

    def __str__(self):
        return self.name
    
    

class Amenity(CommonModel):
    """ Amenity Model Definition """
    name = models.CharField(max_length=150,)
    description = models.TextField(max_length=150, null=True,blank=True,)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Amenities"

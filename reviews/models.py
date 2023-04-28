from django.db import models
from common.models import CommonModel

class Review(CommonModel):
    """Review Model Definition"""
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,related_name="reviews",)

    room = models.ForeignKey("rooms.Room", on_delete=models.SET_NULL, null=True, blank=True,related_name="reviews",)

    experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True,related_name="reviews",)


    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user} / {self.rating} ⭐"

# Create your models here.

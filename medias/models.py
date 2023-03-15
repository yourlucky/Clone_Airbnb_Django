from django.db import models
from common.models import CommonModel


# Create your models here.
class Photo(CommonModel):
    file=models.ImageField()
    description=models.CharField(max_length=140,)
    room=models.ForeignKey("rooms.Room", on_delete=models.CASCADE,)
    experience=models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return f"{self.room.name} Photo"

class Video(CommonModel):
    file=models.FileField()
    experience=models.OneToOneField(
        "experiences.Experience", 
        on_delete=models.CASCADE,
    )

    def __str__ (self):
        return f"{self.experience.name} Video"
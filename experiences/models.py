from django.db import models
from common.models import CommonModel

# Create your models here.

class Experience(CommonModel):
    """Experience Model Definition"""

    country = models.CharField(
        max_length=50, 
        default="한국",
    )

    city = models.CharField(
        max_length=80, 
        default="서울",
    )

    name = models.CharField(max_length=250)
    host = models.ForeignKey(
        "users.User",
         on_delete=models.CASCADE,
    )

    price = models.PositiveBigIntegerField()
    address = models.CharField(
        max_length=250,
    )

    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField(
        max_length=250,
        blank=True,
        null=True,
    )
    perks = models.ManyToManyField("experiences.Perk")

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    
    )

    def __str__(self):
        return self.name





class Perk(CommonModel):
    """What is included in the experience"""

    name = models.CharField(max_length=150,)
    details = models.CharField(max_length=250, blank=True, default="",)
    explanation = models.TextField(blank = True, default="",)

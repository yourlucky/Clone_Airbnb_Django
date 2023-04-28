# Generated by Django 4.1.7 on 2023-03-20 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0005_alter_room_amenities_alter_room_owner"),
        ("experiences", "0003_experience_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reviews",
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

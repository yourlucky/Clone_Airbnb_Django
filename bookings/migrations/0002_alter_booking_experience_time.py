# Generated by Django 4.1.7 on 2023-03-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="experience_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

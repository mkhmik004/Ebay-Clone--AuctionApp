# Generated by Django 5.0.4 on 2024-05-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0006_remove_listing_listing_pic_listing_listing_pic_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_picture_data",
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.URLField(blank=True, null=True),
        ),
    ]
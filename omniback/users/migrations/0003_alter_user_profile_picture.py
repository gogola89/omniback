# Generated by Django 4.2.5 on 2023-11-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_name_user_first_name_user_last_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="default.png",
                null=True,
                upload_to="userprofile",
                verbose_name="User profile image",
            ),
        ),
    ]
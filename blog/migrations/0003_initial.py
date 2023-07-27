# Generated by Django 4.2.2 on 2023-07-26 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("blog", "0002_delete_job"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("pub_date", models.DateTimeField()),
                ("body", models.TextField()),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
    ]

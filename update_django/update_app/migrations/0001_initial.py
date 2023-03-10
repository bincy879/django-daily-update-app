# Generated by Django 4.1.7 on 2023-03-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="update_db",
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
                ("Name", models.CharField(blank=True, max_length=25, null=True)),
                ("Date", models.DateField(blank=True, max_length=20, null=True)),
                ("Workfh", models.CharField(blank=True, max_length=5, null=True)),
                ("Updates", models.CharField(blank=True, max_length=200, null=True)),
                ("Comments", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
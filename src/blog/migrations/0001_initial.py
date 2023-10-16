# Generated by Django 4.2.6 on 2023-10-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Collaborator",
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
                ("name", models.CharField(max_length=128)),
                ("annee", models.IntegerField(default=0)),
                ("job", models.TextField(blank=True)),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="collaborators"),
                ),
            ],
        ),
    ]

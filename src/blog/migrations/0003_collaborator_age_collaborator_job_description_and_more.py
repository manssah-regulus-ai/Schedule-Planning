# Generated by Django 4.2.6 on 2023-10-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_collaborator_magasin"),
    ]

    operations = [
        migrations.AddField(
            model_name="collaborator",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="collaborator",
            name="job_description",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="collaborator",
            name="job",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="collaborator",
            name="magasin",
            field=models.CharField(max_length=128),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-20 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
    ]
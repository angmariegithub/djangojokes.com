# Generated by Django 5.0.1 on 2024-02-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', upload_to='private/resumes'),
        ),
    ]

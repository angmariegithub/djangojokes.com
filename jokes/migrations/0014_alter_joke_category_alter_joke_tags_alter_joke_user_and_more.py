# Generated by Django 5.0.1 on 2024-02-27 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0013_joke_user_alter_joke_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jokes', to='jokes.category'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='jokes', to='jokes.tag'),
        ),
        migrations.AlterField(
            model_name='joke',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='jokes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='JokeVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('joke', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to='jokes.joke')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jokevotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='jokevote',
            constraint=models.UniqueConstraint(fields=('user', 'joke'), name='one_vote_per_user_per_joke'),
        ),
    ]

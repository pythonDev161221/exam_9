# Generated by Django 4.0.3 on 2022-04-02 12:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0006_remove_album_choose_album_choose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='choose',
        ),
        migrations.AddField(
            model_name='photo',
            name='choose',
            field=models.ManyToManyField(related_name='choose_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]

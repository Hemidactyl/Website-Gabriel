# Generated by Django 4.1.3 on 2023-02-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_remove_picture_thumbnail_album_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]

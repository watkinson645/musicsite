# Generated by Django 2.2b1 on 2019-02-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_remove_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='logo',
            field=models.FileField(default='null', upload_to=''),
        ),
    ]
# Generated by Django 2.2b1 on 2019-02-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190212_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favourite',
            field=models.BooleanField(default=False),
        ),
    ]
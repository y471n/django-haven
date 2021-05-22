# Generated by Django 3.2.3 on 2021-05-22 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20210522_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='basemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basemodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

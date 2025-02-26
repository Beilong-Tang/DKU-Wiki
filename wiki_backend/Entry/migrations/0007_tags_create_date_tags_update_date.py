# Generated by Django 4.0.5 on 2023-02-24 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0006_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

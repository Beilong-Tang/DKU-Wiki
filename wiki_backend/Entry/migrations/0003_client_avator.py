# Generated by Django 4.0.5 on 2023-01-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0002_client_entry_updated_diff'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='avator',
            field=models.ImageField(auto_created='default_image.png', default='default_image.png', upload_to='media/avator'),
            preserve_default=False,
        ),
    ]

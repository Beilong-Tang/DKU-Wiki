# Generated by Django 4.0.5 on 2023-02-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0002_alter_client_avator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='avator',
            field=models.ImageField(default='avator/default_image.png', upload_to='avator'),
        ),
    ]

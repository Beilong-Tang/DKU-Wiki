# Generated by Django 4.0.5 on 2023-02-24 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entry', '0004_alter_entry_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='tag',
            field=models.JSONField(),
        ),
    ]

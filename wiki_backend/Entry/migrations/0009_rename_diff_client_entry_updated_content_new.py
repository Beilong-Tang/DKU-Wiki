# Generated by Django 4.1.7 on 2023-04-16 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Entry", "0008_client_nickname"),
    ]

    operations = [
        migrations.RenameField(
            model_name="client_entry_updated",
            old_name="diff",
            new_name="content_new",
        ),
    ]

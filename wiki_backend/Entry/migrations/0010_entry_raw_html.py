# Generated by Django 4.1.7 on 2023-04-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Entry", "0009_rename_diff_client_entry_updated_content_new"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry",
            name="raw_html",
            field=models.TextField(blank=True, null=True),
        ),
    ]

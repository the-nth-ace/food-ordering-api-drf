# Generated by Django 4.1.2 on 2022-10-11 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menufooditem",
            name="menu",
        ),
        migrations.DeleteModel(
            name="Menu",
        ),
    ]

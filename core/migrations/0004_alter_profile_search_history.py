# Generated by Django 4.2.4 on 2023-10-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_search_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='search_history',
            field=models.TextField(blank=True),
        ),
    ]

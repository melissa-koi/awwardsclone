# Generated by Django 3.2.3 on 2021-06-02 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0021_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='rate',
        ),
    ]

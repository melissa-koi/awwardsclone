# Generated by Django 3.2.3 on 2021-06-01 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_auto_20210601_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='content',
            new_name='rate',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='creativity',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='design',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='usability',
        ),
    ]
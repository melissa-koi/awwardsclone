# Generated by Django 3.2.3 on 2021-05-31 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

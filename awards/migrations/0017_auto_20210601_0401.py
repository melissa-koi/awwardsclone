# Generated by Django 3.2.3 on 2021-06-01 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0016_auto_20210601_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='design',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='usability',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
    ]

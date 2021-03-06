# Generated by Django 3.2.3 on 2021-06-01 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0008_auto_20210601_0306'),
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
        migrations.AlterField(
            model_name='rate',
            name='website',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.website'),
        ),
    ]

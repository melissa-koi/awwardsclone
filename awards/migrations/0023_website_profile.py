# Generated by Django 3.2.3 on 2021-06-02 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0022_remove_rate_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.profile'),
        ),
    ]
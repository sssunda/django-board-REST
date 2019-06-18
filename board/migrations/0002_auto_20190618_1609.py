# Generated by Django 2.2.2 on 2019-06-18 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posting',
            name='modified_date',
            field=models.DateField(auto_now=True),
        ),
    ]
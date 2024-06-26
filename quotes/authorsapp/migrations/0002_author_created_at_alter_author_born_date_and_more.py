# Generated by Django 5.0.4 on 2024-04-20 14:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=150),
        ),
    ]

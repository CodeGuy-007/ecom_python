# Generated by Django 4.0.6 on 2023-01-12 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_order_details_order_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2023, 1, 12, 18, 34, 30, 17041)),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_at',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

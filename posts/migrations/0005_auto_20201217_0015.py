# Generated by Django 3.1.3 on 2020-12-16 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20201217_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 18, 15, 43, 704919, tzinfo=utc)),
        ),
    ]

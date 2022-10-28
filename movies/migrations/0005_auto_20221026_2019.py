# Generated by Django 3.1 on 2022-10-26 20:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20221023_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmwork',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='filmwork',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769071, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769071, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769055, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 26, 20, 19, 23, 769071, tzinfo=utc)),
        ),
    ]

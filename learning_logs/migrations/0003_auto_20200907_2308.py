# Generated by Django 3.1.1 on 2020-09-07 23:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_testmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 7, 23, 7, 49, 44249, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='text',
            field=models.CharField(default='test', max_length=200),
            preserve_default=False,
        ),
    ]
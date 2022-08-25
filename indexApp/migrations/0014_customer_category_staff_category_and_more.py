# Generated by Django 4.0.1 on 2022-05-07 19:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0013_staff_username_alter_reservation_createddate_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='category',
            field=models.CharField(default='Customer', max_length=8),
        ),
        migrations.AddField(
            model_name='staff',
            name='category',
            field=models.CharField(default='staff', max_length=5),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='CreatedDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 5, 7, 19, 35, 31, 416678, tzinfo=utc)),
        ),
    ]

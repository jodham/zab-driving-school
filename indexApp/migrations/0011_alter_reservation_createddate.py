# Generated by Django 4.0.1 on 2022-02-21 21:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0010_remove_customer_license_type_customer_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='CreatedDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 2, 21, 21, 32, 21, 992002, tzinfo=utc)),
        ),
    ]

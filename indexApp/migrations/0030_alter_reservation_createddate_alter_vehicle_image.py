# Generated by Django 4.0.1 on 2022-09-09 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0029_alter_application_id_alter_profile_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='CreatedDate',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 9, 9, 20, 2, 35, 489554, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='static/media'),
        ),
    ]

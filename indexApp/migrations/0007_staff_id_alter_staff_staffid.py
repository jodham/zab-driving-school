# Generated by Django 4.0.1 on 2022-02-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0006_alter_jobtitle_job_titledesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='staffId',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0002_alter_mailings_time_end_alter_mailings_time_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailings',
            name='time_end',
            field=models.DateTimeField(verbose_name='время конца рассылки'),
        ),
        migrations.AlterField(
            model_name='mailings',
            name='time_start',
            field=models.DateTimeField(verbose_name='время начала рассылки'),
        ),
    ]
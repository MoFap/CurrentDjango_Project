# Generated by Django 3.2.3 on 2021-05-31 15:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year_of_graduation',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 15, 33, 19, 974341, tzinfo=utc)),
        ),
    ]
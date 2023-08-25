# Generated by Django 3.2.5 on 2023-08-09 11:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_auto_20230809_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 536989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 536989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 522985, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 520984, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 520984, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 520984, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 521987, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 11, 46, 57, 521987, tzinfo=utc)),
        ),
    ]
# Generated by Django 3.2.5 on 2023-08-09 10:46

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 46909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categories'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 46909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 34906, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 33886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 33886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 33886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 34906, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 10, 46, 25, 34906, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.2.5 on 2023-08-09 16:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_auto_20230809_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 890181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 890181, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='collection',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 878159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='product_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product'),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 877158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 877158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 877158, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 878159, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='variant',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 16, 8, 11, 878159, tzinfo=utc)),
        ),
    ]
# Generated by Django 3.2.5 on 2023-08-10 04:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0016_auto_20230810_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]

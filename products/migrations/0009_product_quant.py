# Generated by Django 4.1.3 on 2022-12-08 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quant',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.0 on 2022-10-28 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_rename_created_by_cart_addcart_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_by',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

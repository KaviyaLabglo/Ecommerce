# Generated by Django 4.0 on 2022-10-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_alter_cart_created_on_alter_order_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_order_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_product_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_tax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Success'), (2, 'Pending'), (0, 'FAILED')], default='Success', max_length=200),
        ),
    ]

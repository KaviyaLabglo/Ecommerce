# Generated by Django 4.0 on 2022-11-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0049_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='updated_quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Success'), (2, 'Pending'), (0, 'Cancel')], default=2),
        ),
    ]

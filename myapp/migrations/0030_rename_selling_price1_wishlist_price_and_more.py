# Generated by Django 4.0 on 2022-10-28 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_rename_is_active_wishlist_is_active1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='selling_price1',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='addwhitelist_by',
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-31 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='items',
        ),
    ]

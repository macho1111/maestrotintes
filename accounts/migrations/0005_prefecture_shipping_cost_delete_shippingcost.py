# Generated by Django 4.2.11 on 2024-04-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maruko', '0013_remove_product_prefecture_shipping_cost'),
        ('accounts', '0004_alter_user_prefecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='prefecture',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='送料'),
        ),
        migrations.DeleteModel(
            name='ShippingCost',
        ),
    ]
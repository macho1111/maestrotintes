# Generated by Django 4.2.11 on 2024-04-13 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_prefecture'),
        ('maruko', '0011_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prefecture_shipping_cost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.shippingcost', verbose_name='送料'),
        ),
    ]

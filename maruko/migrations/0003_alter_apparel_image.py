# Generated by Django 4.2.11 on 2024-04-01 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maruko', '0002_apparel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparel',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='apparel_images/'),
        ),
    ]
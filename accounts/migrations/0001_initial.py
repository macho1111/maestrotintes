# Generated by Django 4.2.11 on 2024-04-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Eメールアドレス')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='名前')),
                ('furigana', models.CharField(blank=True, max_length=255, null=True, verbose_name='フリガナ')),
                ('address', models.TextField(blank=True, null=True, verbose_name='住所')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='電話番号')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

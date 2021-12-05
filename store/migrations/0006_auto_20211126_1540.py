# Generated by Django 3.2.5 on 2021-11-26 12:40

import django.contrib.auth.base_user
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211126_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=django.contrib.auth.models.User.get_email_field_name, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default=django.contrib.auth.base_user.AbstractBaseUser.get_username, max_length=100, null=True),
        ),
    ]

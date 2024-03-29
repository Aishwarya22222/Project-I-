# Generated by Django 4.2.1 on 2024-03-08 09:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Total_price',
            new_name='total_price',
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(15)]),
        ),
    ]

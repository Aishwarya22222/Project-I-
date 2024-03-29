# Generated by Django 4.2.1 on 2024-02-05 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_image', models.CharField(max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

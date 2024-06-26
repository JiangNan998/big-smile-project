# Generated by Django 5.0.6 on 2024-06-13 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigsmile', '0003_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productinfo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bigsmile.productinfo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/'),
        ),
    ]

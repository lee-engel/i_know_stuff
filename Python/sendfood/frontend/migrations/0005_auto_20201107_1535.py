# Generated by Django 3.1.3 on 2020-11-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20201107_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='special_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4),
        ),
    ]

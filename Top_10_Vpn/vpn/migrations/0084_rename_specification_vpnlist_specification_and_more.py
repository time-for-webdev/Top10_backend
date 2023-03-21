# Generated by Django 4.1.7 on 2023-03-21 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0083_alter_specification_vpn_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vpnlist',
            old_name='Specification',
            new_name='specification',
        ),
        migrations.AlterField(
            model_name='vpnlist',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='vpnlist',
            name='user_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
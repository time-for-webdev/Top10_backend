# Generated by Django 4.1.7 on 2023-03-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0074_alter_device_unique_together_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='top_ten',
            constraint=models.UniqueConstraint(fields=('First', 'Second', 'Third', 'Forth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth'), name='unique_top_ten'),
        ),
    ]
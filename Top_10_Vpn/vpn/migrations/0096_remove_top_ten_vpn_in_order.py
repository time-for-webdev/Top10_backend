# Generated by Django 4.1.7 on 2023-03-28 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0095_top_ten_vpn_in_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='top_ten',
            name='vpn_in_order',
        ),
    ]

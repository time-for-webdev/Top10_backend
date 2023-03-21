# Generated by Django 4.1.7 on 2023-03-21 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0081_specification_remove_vpnlist_specification1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='vpn_name',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='specification',
            name='id',
            field=models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]

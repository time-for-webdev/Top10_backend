# Generated by Django 4.1.7 on 2023-03-18 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0012_toptenlist_delete_topten'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toptenlist',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vpn.location'),
        ),
    ]

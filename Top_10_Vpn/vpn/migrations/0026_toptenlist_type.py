# Generated by Django 4.1.7 on 2023-03-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0025_remove_toptenlist_type_toptenlist_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='toptenlist',
            name='type',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='vpn.all_avilable_filter'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-18 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0036_delete_toptenlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopTenList',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('first', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vpn.vpnlist')),
                ('type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vpn.all_avilable_filter')),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-18 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0039_alter_all_avilable_filter_id_alter_vpnlist_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_ten',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vpn.all_avilable_filter')),
            ],
        ),
    ]
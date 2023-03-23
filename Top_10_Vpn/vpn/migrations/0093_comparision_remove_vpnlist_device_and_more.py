# Generated by Django 4.1.7 on 2023-03-23 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0092_alter_vpnlist_riben_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comparision',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('vpn', models.CharField(max_length=1000, unique=True)),
                ('comparison_description', models.TextField()),
                ('moneybackguarantee', models.CharField(default='', max_length=1000)),
                ('servers_or_countries', models.CharField(default='', max_length=1000)),
                ('killswitch', models.CharField(default='', max_length=1000)),
                ('number_of_device_or_licence', models.IntegerField(default=0)),
                ('mobile', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='vpnlist',
            name='Device',
        ),
        migrations.RemoveField(
            model_name='vpnlist',
            name='coutries_allowed',
        ),
        migrations.RemoveField(
            model_name='vpnlist',
            name='killswitch',
        ),
        migrations.RemoveField(
            model_name='vpnlist',
            name='moneybackguarantee',
        ),
        migrations.RemoveField(
            model_name='vpnlist',
            name='number_of_device_or_licence',
        ),
        migrations.AddField(
            model_name='vpnlist',
            name='Comparision',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='vpn.comparision'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-18 12:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0014_alter_toptenlist_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_avilable_filter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='toptenlist',
            name='type',
        ),
        migrations.AddField(
            model_name='toptenlist',
            name='Type',
            field=models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, to='vpn.all_avilable_filter'),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vpn.all_avilable_filter'),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vpn.all_avilable_filter'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vpn.all_avilable_filter'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0098_alter_device_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(choices=[('good', 'bad')], max_length=100, unique=True),
        ),
    ]

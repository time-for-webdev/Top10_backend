# Generated by Django 4.1.7 on 2023-05-25 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0022_service_first_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(choices=[('Android', 'Android'), ('iPhone&iPad', 'iPhone&iPad'), ('Mac', 'Mac'), ('Routers', 'Routers'), ('Pc', 'Pc'), ('Windows', 'Windows')], max_length=200, unique=True),
        ),
    ]

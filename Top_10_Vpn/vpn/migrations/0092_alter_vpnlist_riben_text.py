# Generated by Django 4.1.7 on 2023-03-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0091_rename_remarks_remark_rename_remark_remark_remarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vpnlist',
            name='riben_text',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
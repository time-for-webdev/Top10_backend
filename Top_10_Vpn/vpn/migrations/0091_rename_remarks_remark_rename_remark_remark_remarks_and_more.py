# Generated by Django 4.1.7 on 2023-03-23 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0090_remarks_vpnlist_riben_text_vpnlist_remarks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='remarks',
            new_name='remark',
        ),
        migrations.RenameField(
            model_name='remark',
            old_name='remark',
            new_name='remarks',
        ),
        migrations.RenameField(
            model_name='vpnlist',
            old_name='remarks',
            new_name='remark',
        ),
    ]

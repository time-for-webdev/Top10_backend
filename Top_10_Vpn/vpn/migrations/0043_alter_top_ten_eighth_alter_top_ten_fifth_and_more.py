# Generated by Django 4.1.7 on 2023-03-18 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0042_top_ten_eighth_top_ten_fifth_top_ten_forth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_ten',
            name='Eighth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_eight_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Fifth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_fifth_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='First',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_first_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Forth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_forth_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Ninth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_ninth_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_second_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Seventh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_seventh_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Sixth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_sexth_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Tenth',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_tenth_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='Third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='top_ten_third_set', to='vpn.vpnlist'),
        ),
        migrations.AlterField(
            model_name='top_ten',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vpn.all_avilable_filter'),
        ),
    ]

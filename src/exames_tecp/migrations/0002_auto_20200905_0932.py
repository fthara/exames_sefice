# Generated by Django 2.0.7 on 2020-09-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames_tecp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exame_tecp',
            name='Borg',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Borg'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exame_tecp',
            name='Delta_FC_VO2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Delta FC/VO2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exame_tecp',
            name='Delta_VE_VCO2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Delta VE/VCO2MC'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exame_tecp',
            name='Delta_VO2_W',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Delta VO2/W'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exame_tecp',
            name='SpO2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='SpO2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exame_tecp',
            name='VE_VVM',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='VE/VVM'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210313_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurs',
            name='acc_no',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Account Number (NUBAN)'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='bank_name',
            field=models.CharField(blank=True, choices=[('', 'SELECT BANK'), ('ACCESS BANK PLC', 'ACCESS BANK PLC'), ('CITIBANK NIG. PLC', 'CITIBANK NIG. PLC'), ('ECOBANK NIG. PLC', 'ECOBANK NIG. PLC'), ('FIDELITY BANK PLC', 'FIDELITY BANK PLC'), ('FIRST BANK NIG. LTD', 'FIRST BANK NIG. LTD'), ('FIRST CITY MONUMENT BANK PLC', 'FIRST CITY MONUMENT BANK PLC'), ('GLOBUS BANK LTD', 'GLOBUS BANK LTD'), ('GUARANTY TRUST BANK PLC', 'GUARANTY TRUST BANK PLC'), ('HERITAGE BANKING COMPANY LTD', 'HERITAGE BANKING COMPANY LTD'), ('KEYSTONE BANK', 'KEYSTONE BANK'), ('POLARIS BANK', 'POLARIS BANK'), ('PROVIDUS BANK', 'PROVIDUS BANK'), ('STANBIC IBTC BANK LTD', 'STANBIC IBTC BANK LTD'), ('STANDARD CHARTERED BANK NIG. LTD', 'STANDARD CHARTERED BANK NIG. LTD'), ('STERLING BANK PLC', 'STERLING BANK PLC'), ('SUNTRUST BANK NIG. PLC', 'SUNTRUST BANK NIG. PLC'), ('TITAN TRUST BANK LTD', 'TITAN TRUST BANK LTD'), ('UNION BANK OF NIG. PLC', 'UNION BANK OF NIG. PLC'), ('UNITED BANK FOR AFRICA PLC', 'UNITED BANK FOR AFRICA PLC'), ('UNITY BANK PLC', 'UNITY BANK PLC'), ('WEMA BANK PLC', 'WEMA BANK PLC'), ('ZENITH BANK PLC', 'ZENITH BANK PLC')], max_length=255, null=True, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='bvn',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Bank Verification Number (BVN)'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='lga',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Local Government Area (LGA)'),
        ),
    ]

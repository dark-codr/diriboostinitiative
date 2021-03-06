# Generated by Django 3.1.7 on 2021-03-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20210318_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrepreneurs',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='mid_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='entrepreneurs',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Phone Number'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-09-30 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0005_alter_wallet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=15),
        ),
    ]

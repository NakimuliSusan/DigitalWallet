# Generated by Django 4.0.6 on 2022-09-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_alter_receipt_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('F', 'Inactive')], max_length=15),
        ),
    ]

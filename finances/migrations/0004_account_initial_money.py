# Generated by Django 3.1.6 on 2021-12-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_transaction_transfer_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='initial_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

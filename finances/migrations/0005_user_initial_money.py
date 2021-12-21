# Generated by Django 3.1.6 on 2021-12-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_account_initial_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='initial_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
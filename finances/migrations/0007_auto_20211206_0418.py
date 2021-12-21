# Generated by Django 3.1.6 on 2021-12-06 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0006_auto_20211205_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit'), ('Family', 'Family'), ('Food', 'Food'), ('Friends', 'Friends'), ('Gas', 'Gas'), ('Groceries', 'Groceries'), ('Shopping', 'Shopping'), ('Savings', 'Savings'), ('School', 'School'), ('Work', 'Work'), ('Other', 'Other')], default='Other', max_length=12),
        ),
    ]
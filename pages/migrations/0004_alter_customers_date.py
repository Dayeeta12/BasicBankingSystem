# Generated by Django 3.2.6 on 2021-09-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_customers_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
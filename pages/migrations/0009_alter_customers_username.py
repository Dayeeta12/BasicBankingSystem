# Generated by Django 3.2.6 on 2021-09-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210906_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]

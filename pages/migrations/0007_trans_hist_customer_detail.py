# Generated by Django 3.2.6 on 2021-09-06 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_trans_hist'),
    ]

    operations = [
        migrations.AddField(
            model_name='trans_hist',
            name='customer_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.customers'),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-16 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keshoapp', '0002_babe_b_taker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_number', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='UGX', max_length=5, null=True)),
                ('payment_cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoapp.categorystay')),
            ],
        ),
        migrations.AddField(
            model_name='babe',
            name='fee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='keshoapp.pay'),
        ),
    ]

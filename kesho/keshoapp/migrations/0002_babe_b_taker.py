# Generated by Django 5.0.3 on 2024-04-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keshoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='babe',
            name='b_taker',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-06 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

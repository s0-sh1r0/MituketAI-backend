# Generated by Django 5.1.3 on 2024-12-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_item_id_alter_register_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='point',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.6 on 2024-08-14 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_topology_views', '0009_individualoptions_group_virtualchassis'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualoptions',
            name='grid_size',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

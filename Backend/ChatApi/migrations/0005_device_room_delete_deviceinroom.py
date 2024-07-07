# Generated by Django 5.0.6 on 2024-07-06 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "ChatApi",
            "0004_alter_device_created_time_alter_device_last_visited_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="device",
            name="room",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="room_code",
                to="ChatApi.roomcode",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="DeviceInRoom",
        ),
    ]
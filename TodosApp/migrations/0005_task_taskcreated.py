# Generated by Django 4.1.6 on 2023-02-10 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TodosApp", "0004_remove_task_taskcreated"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="taskCreated",
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]

# Generated by Django 4.2.1 on 2024-04-21 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_tasks_delete_task'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
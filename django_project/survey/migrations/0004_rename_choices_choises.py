# Generated by Django 4.1 on 2022-09-02 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_rename_choice_choices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='Choises',
        ),
    ]

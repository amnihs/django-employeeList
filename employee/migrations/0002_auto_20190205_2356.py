# Generated by Django 2.1.5 on 2019-02-05 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='lst_name',
            new_name='last_name',
        ),
    ]

# Generated by Django 2.2.2 on 2019-12-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0010_auto_20191218_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstate',
            old_name='state_context_saved',
            new_name='context',
        ),
    ]
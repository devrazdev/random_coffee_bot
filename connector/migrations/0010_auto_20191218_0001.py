# Generated by Django 2.2.2 on 2019-12-17 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0009_auto_20191217_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='state_context_saved',
        ),
        migrations.CreateModel(
            name='UserState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_context_saved', models.CharField(default="{'name': 'NullState', 'params': {}}", max_length=500)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connector.User')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userstate',
            constraint=models.UniqueConstraint(fields=('user',), name='unique_user_state'),
        ),
    ]

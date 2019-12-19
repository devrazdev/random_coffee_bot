# Generated by Django 2.2.2 on 2019-12-15 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('connector', '0003_auto_20191215_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='cancel_reason',
            field=models.CharField(blank=True, choices=[('', '-'), ('NT', 'Вряд ли найду время'), ('NIM', 'Не в настроении'), ('NI', 'Что-то неинтересно...')], max_length=100),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user_a_meeting_failure_reason',
            field=models.CharField(blank=True, choices=[('DC', 'Партнер не вышел на связь'), ('CA', 'Не смогли договориться когда/где'), ('FM', 'Форс-мажор')], max_length=100),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user_b_meeting_failure_reason',
            field=models.CharField(blank=True, choices=[('DC', 'Партнер не вышел на связь'), ('CA', 'Не смогли договориться когда/где'), ('FM', 'Форс-мажор')], max_length=100),
        ),
    ]
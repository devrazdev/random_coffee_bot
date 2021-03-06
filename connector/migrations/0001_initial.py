# Generated by Django 2.2.2 on 2019-12-14 17:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.BooleanField(null=True)),
                ('text', models.CharField(max_length=300)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('year', models.IntegerField()),
                ('accepted', models.BooleanField(null=True)),
                ('cancel_reason', models.CharField(choices=[('', '-'), ('NT', 'Вряд ли найду время'), ('NIM', 'Не в настроении'), ('NI', 'Что-то неинтересно...')], max_length=100)),
                ('message_id', models.CharField(blank=True, max_length=100)),
                ('counter', models.IntegerField(default=0)),
                ('first_time_sent_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('decided_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('year', models.IntegerField()),
                ('user_a_telegram_id', models.CharField(max_length=100)),
                ('user_b_telegram_id', models.CharField(max_length=100)),
                ('user_a_meeting_took_place', models.BooleanField(null=True)),
                ('user_b_meeting_took_place', models.BooleanField(null=True)),
                ('user_a_meeting_failure_reason', models.CharField(max_length=300)),
                ('user_b_meeting_failure_reason', models.CharField(max_length=300)),
                ('user_a_happy', models.BooleanField(null=True)),
                ('user_b_happy', models.BooleanField(null=True)),
                ('message_id', models.CharField(blank=True, max_length=100)),
                ('sent_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(editable=False, max_length=100)),
                ('random_coffee_bot_telegram_username', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('type', models.CharField(choices=[('I', 'Один'), ('T', 'С коллегами')], max_length=100)),
                ('about', models.CharField(blank=True, max_length=300)),
                ('telegram_username', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('meeting_frequency', models.CharField(choices=[('H', 'Два и более раз в неделю 🐆'), ('M', 'Раз в неделю 🐇'), ('L', 'Раз в две недели 🐢')], max_length=100)),
                ('meeting_motivation', models.CharField(choices=[('D', 'Найти вторую половину ❤'), ('N', 'Поговорить о работе'), ('HF', 'Просто отдохнуть')], max_length=100)),
                ('state_saved', models.CharField(default='NullState', max_length=100)),
                ('first_time_visited_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('registered_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='connector.Group')),
            ],
        ),
        migrations.AddConstraint(
            model_name='meeting',
            constraint=models.UniqueConstraint(fields=('week', 'year', 'user_a_telegram_id', 'user_b_telegram_id'), name='unique_meeting'),
        ),
        migrations.AddField(
            model_name='invitation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connector.User'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='connector.User'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('telegram_id', 'random_coffee_bot_telegram_username'), name='unique_registered_user'),
        ),
        migrations.AddConstraint(
            model_name='invitation',
            constraint=models.UniqueConstraint(fields=('user', 'week', 'year'), name='unique_week_invitation'),
        ),
    ]

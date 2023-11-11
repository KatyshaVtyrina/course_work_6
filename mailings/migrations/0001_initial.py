# Generated by Django 4.2.6 on 2023-11-10 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.DateTimeField(verbose_name='время начала рассылки')),
                ('time_end', models.DateTimeField(verbose_name='время конца рассылки')),
                ('frequency', models.TextField(choices=[('DAILY', 'Раз в день'), ('WEEKLY', 'Раз в неделю'), ('MONTHLY', 'Раз в месяц')], max_length=10, verbose_name='периодичность')),
                ('status', models.TextField(choices=[('CREATED', 'Создана'), ('STARTED', 'Запущена'), ('FINISHED', 'Завершена')], default='CREATED', max_length=10, verbose_name='статус')),
                ('clients', models.ManyToManyField(to='mailings.client', verbose_name='клиенты')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='тема письма')),
                ('body', models.TextField(verbose_name='тело письма')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
            },
        ),
        migrations.CreateModel(
            name='MailingsLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='дата и время попытки')),
                ('status', models.TextField(choices=[('SENT', 'Отправлено'), ('FAILED', 'Не удалось отправить')], verbose_name='статус попытки')),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='ответ почтового сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailings', verbose_name='рассылка')),
            ],
            options={
                'verbose_name': 'лог отправки письма',
                'verbose_name_plural': 'логи отправки писем',
            },
        ),
        migrations.AddField(
            model_name='mailings',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.message', verbose_name='тема письма'),
        ),
        migrations.AddField(
            model_name='mailings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]

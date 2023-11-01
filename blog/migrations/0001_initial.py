# Generated by Django 4.2.6 on 2023-11-01 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('-created_at',),
            },
        ),
    ]

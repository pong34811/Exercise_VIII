# Generated by Django 5.0.7 on 2024-07-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anime_order', models.IntegerField()),
                ('anime_name_th', models.CharField(max_length=100)),
                ('anime_name_en', models.CharField(max_length=100)),
                ('anime_seasons', models.IntegerField()),
                ('anime_channel', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2020-01-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0023_auto_20200106_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Russia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Русский язык',
                'verbose_name_plural': 'Русский язык',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Обществознание',
                'verbose_name_plural': 'Обществознание',
            },
        ),
    ]

# Generated by Django 2.1.3 on 2019-03-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0011_auto_20190302_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='fiveth',
            field=models.TextField(blank=True, verbose_name='Пятый ответ'),
        ),
        migrations.AddField(
            model_name='task',
            name='sixth',
            field=models.TextField(blank=True, verbose_name='Шестой ответ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='forth',
            field=models.TextField(verbose_name='Четвертый ответ'),
        ),
    ]

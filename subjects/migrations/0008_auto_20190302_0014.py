# Generated by Django 2.1.3 on 2019-03-01 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0007_auto_20190302_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, default='', upload_to='subjects/static/media', verbose_name='Картинка (название с расширением)'),
        ),
    ]

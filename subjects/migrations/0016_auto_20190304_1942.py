# Generated by Django 2.1.3 on 2019-03-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0015_auto_20190304_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, upload_to='img', verbose_name='Картинка'),
        ),
    ]

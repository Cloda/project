# Generated by Django 2.1.3 on 2019-03-04 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0014_auto_20190302_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/', verbose_name='Картинка'),
        ),
    ]

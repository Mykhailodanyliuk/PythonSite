# Generated by Django 3.1.7 on 2021-02-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товари'},
        ),
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата добавлення'),
        ),
    ]

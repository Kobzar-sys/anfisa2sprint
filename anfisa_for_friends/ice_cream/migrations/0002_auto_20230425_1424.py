# Generated by Django 3.2.16 on 2023-04-25 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='icecream',
            options={'verbose_name': 'Морроженное', 'verbose_name_plural': 'Морроженные'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Топинг', 'verbose_name_plural': 'Топинги'},
        ),
        migrations.AlterModelOptions(
            name='wrapper',
            options={'verbose_name': 'Обертка', 'verbose_name_plural': 'Обертки'},
        ),
    ]

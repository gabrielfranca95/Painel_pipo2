# Generated by Django 4.0.3 on 2022-03-27 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Acme_Ceo', '0002_alter_dental_sorriso_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dental_sorriso',
            options={'verbose_name': 'Usuario do plano', 'verbose_name_plural': 'Dental Sorriso'},
        ),
        migrations.AlterModelOptions(
            name='norte_europa',
            options={'verbose_name': 'Usuario do plano', 'verbose_name_plural': 'Norte Europa'},
        ),
    ]

# Generated by Django 3.2.4 on 2021-12-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
# Generated by Django 3.1 on 2020-08-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artesanoapp', '0002_auto_20200811_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]

# Generated by Django 2.1.7 on 2019-02-28 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20190228_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='size',
            field=models.FloatField(),
        ),
    ]

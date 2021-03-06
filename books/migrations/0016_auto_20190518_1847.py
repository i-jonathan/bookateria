# Generated by Django 2.2.1 on 2019-05-18 18:47

import books.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_auto_20190518_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ('title',)},
        ),
        migrations.AddField(
            model_name='books',
            name='typology',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='books.Type'),
        ),
        migrations.AlterField(
            model_name='books',
            name='downloads',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='books',
            name='pdf',
            field=models.FileField(upload_to=books.models.Document.path_and_rename),
        ),
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='books',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.1.1 on 2020-11-13 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
# Generated by Django 3.2.13 on 2022-11-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='adult',
            field=models.BooleanField(default=True),
        ),
    ]
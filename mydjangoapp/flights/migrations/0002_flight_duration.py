# Generated by Django 4.1.6 on 2023-02-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='duration',
            field=models.IntegerField(default=0),
        ),
    ]

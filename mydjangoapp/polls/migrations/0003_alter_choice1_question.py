# Generated by Django 4.1.6 on 2023-02-10 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice1_delete_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice1',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-13 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_form_telegram'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='age',
        ),
    ]

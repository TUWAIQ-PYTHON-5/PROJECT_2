# Generated by Django 4.1.6 on 2023-02-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raghad', '0002_sign_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sign_up',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]

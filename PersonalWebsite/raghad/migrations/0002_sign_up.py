# Generated by Django 4.1.6 on 2023-02-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raghad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('email', models.TextField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]

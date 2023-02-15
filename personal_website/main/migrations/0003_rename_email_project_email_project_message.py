# Generated by Django 4.1.6 on 2023-02-12 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_description_project_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='project',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]

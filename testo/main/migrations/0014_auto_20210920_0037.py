# Generated by Django 2.2.24 on 2021-09-20 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210920_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='user',
        ),
    ]

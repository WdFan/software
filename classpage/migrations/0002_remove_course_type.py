# Generated by Django 3.1.3 on 2021-12-26 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classpage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='type',
        ),
    ]

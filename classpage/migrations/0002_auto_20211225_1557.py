# Generated by Django 3.1.3 on 2021-12-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20211225_1211'),
        ('classpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(related_name='course', to='login.loginUser'),
        ),
    ]

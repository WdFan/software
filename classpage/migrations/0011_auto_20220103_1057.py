# Generated by Django 3.1.3 on 2022-01-03 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classpage', '0010_auto_20211227_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='simple_name',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classpage', '0008_auto_20211227_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='banji',
            name='code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
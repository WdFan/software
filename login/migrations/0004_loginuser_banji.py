# Generated by Django 3.1.3 on 2021-12-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classpage', '0003_banji_color'),
        ('login', '0003_auto_20211226_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='banji',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banji', to='classpage.banji'),
        ),
    ]

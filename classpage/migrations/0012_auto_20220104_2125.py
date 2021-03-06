# Generated by Django 3.1.3 on 2022-01-04 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classpage', '0011_auto_20220103_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banji',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.IntegerField(default=0)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('msg', models.CharField(blank=True, max_length=200)),
                ('banji', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='classpage.banji')),
            ],
        ),
    ]

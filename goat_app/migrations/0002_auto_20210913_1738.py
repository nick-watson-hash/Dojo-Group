# Generated by Django 2.2 on 2021-09-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goat_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bank',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='enter name', max_length=25),
        ),
    ]

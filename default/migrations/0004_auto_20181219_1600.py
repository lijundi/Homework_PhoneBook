# Generated by Django 2.1.3 on 2018-12-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_linkman'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkman',
            name='img',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='linkman',
            name='mail',
            field=models.CharField(default='', max_length=20),
        ),
    ]

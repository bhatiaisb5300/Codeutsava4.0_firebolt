# Generated by Django 2.1.7 on 2020-01-19 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200119_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]

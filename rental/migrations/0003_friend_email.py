# Generated by Django 3.2.4 on 2021-07-13 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_auto_20210713_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]

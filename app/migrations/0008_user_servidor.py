# Generated by Django 2.2.7 on 2020-03-06 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200306_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='servidor',
            field=models.BooleanField(default=False),
        ),
    ]

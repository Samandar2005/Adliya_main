# Generated by Django 4.1 on 2022-09-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='icon',
            field=models.IntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
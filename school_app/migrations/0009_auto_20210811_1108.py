# Generated by Django 3.2.6 on 2021-08-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0008_auto_20210811_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='contact',
            field=models.IntegerField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.IntegerField(max_length=13, null=True),
        ),
    ]

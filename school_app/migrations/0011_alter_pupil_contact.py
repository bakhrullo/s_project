# Generated by Django 3.2.6 on 2021-08-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0010_auto_20210811_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='contact',
            field=models.PositiveIntegerField(max_length=13, null=True),
        ),
    ]

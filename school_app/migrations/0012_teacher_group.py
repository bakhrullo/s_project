# Generated by Django 3.2.6 on 2021-08-11 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('school_app', '0011_alter_pupil_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.group'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-09 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0004_remove_teacher_teach_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teach_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school_app.grade'),
        ),
    ]
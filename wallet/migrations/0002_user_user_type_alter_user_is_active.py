# Generated by Django 4.2.5 on 2023-11-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher'), ('admin', 'Admin')], default='student', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

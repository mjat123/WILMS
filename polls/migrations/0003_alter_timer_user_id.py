# Generated by Django 4.1 on 2023-12-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_useraccountmodel_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='user_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2.5 on 2023-12-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='isOverstayingCharged',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
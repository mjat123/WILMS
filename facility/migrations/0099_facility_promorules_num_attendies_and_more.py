# Generated by Django 4.2.5 on 2023-12-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0098_alter_facility_facilityname'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility_promorules',
            name='num_attendies',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='facility_promorules',
            name='num_pc',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='facility_promorules_set',
            name='num_attendies',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='facility_promorules_set',
            name='num_pc',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='facility_promorules',
            name='capacity',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='facility_promorules',
            name='new_rate',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='facility_promorules_set',
            name='capacity',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='facility_promorules_set',
            name='new_rate',
            field=models.FloatField(default=None),
        ),
    ]
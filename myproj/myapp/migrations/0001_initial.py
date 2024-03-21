# Generated by Django 5.0.2 on 2024-03-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_code', models.IntegerField()),
                ('train_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('distance', models.IntegerField()),
                ('starting_time', models.IntegerField()),
                ('ending_time', models.IntegerField()),
                ('start_station_code', models.IntegerField()),
                ('end_station_code', models.IntegerField()),
                ('frequency', models.IntegerField()),
            ],
        ),
    ]
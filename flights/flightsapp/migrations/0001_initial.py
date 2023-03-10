# Generated by Django 4.1.5 on 2023-01-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no', models.CharField(max_length=6)),
                ('time', models.TimeField()),
                ('origin', models.CharField(max_length=45)),
                ('remarks', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_no', models.CharField(max_length=6)),
                ('time', models.TimeField()),
                ('to', models.CharField(max_length=45)),
                ('gate', models.CharField(max_length=2)),
                ('remarks', models.CharField(max_length=45)),
            ],
        ),
    ]

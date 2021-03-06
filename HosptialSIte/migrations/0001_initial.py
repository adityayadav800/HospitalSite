# Generated by Django 3.0.6 on 2020-05-17 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=200)),
                ('patient_illness', models.TextField()),
                ('admit_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('discharge_date', models.DateTimeField(blank=True, null=True)),
                ('attending_doctor_name', models.CharField(max_length=200)),
                ('allocated_bed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_beds', models.IntegerField(default=0)),
                ('total_nonMed_staff', models.IntegerField(default=0)),
            ],
        ),
    ]

# Generated by Django 2.0.dev20170322162159 on 2017-04-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_crew'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_first_name', models.CharField(max_length=15)),
                ('u_middle_name', models.CharField(max_length=15)),
                ('u_last_name', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('manager', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='crew',
            old_name='first_name',
            new_name='c_first_name',
        ),
        migrations.RenameField(
            model_name='crew',
            old_name='last_name',
            new_name='c_last_name',
        ),
    ]

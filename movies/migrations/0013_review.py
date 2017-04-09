# Generated by Django 2.0.dev20170322162159 on 2017-04-07 04:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20170406_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('m_id', models.ManyToManyField(to='movies.Movie')),
                ('u_id', models.ManyToManyField(to='movies.User')),
            ],
        ),
    ]

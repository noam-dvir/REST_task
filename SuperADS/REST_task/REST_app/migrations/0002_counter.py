# Generated by Django 2.2.1 on 2019-08-12 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-08-11 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15)),
                ('ua', models.CharField(max_length=256)),
                ('val', models.IntegerField()),
            ],
        ),
    ]
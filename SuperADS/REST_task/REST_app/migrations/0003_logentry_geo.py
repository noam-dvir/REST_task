# Generated by Django 2.2.1 on 2019-08-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('REST_app', '0002_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='geo',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]

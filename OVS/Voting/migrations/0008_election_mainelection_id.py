# Generated by Django 3.2 on 2021-07-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Voting', '0007_auto_20210715_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='MainElection_id',
            field=models.BigIntegerField(default=0),
        ),
    ]

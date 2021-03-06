# Generated by Django 4.0.3 on 2022-03-24 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passanger',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('rewardPoints', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]

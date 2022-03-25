# Generated by Django 4.0.1 on 2022-03-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('ratings', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='Passanger',
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
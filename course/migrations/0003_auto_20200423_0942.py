# Generated by Django 3.0.4 on 2020-04-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
# Generated by Django 3.1.2 on 2020-12-21 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=0, help_text='Add course description', max_length=1000),
            preserve_default=False,
        ),
    ]
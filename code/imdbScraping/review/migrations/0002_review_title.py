# Generated by Django 2.1.4 on 2018-12-08 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]

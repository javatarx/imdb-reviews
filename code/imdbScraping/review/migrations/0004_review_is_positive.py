# Generated by Django 2.1.4 on 2018-12-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_positive',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2022-04-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220409_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='agm',
            name='commission',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='dm',
            name='commission',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='gm',
            name='commission',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rgm',
            name='commission',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

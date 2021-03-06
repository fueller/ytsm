# Generated by Django 2.1.2 on 2018-10-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YtManagerApp', '0002_subscriptionfolder_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='rating',
            field=models.FloatField(default=0.5),
        ),
        migrations.AddField(
            model_name='video',
            name='uploader_name',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]

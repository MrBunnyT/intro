# Generated by Django 3.1.2 on 2020-10-02 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_tweet_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='images',
            new_name='image',
        ),
    ]

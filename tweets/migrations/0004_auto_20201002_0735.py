# Generated by Django 3.1.2 on 2020-10-02 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20201002_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='likes',
            field=models.BigIntegerField(blank=True, default=0, null=True),
        ),
    ]

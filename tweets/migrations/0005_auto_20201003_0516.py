# Generated by Django 3.1.2 on 2020-10-02 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20201002_0735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-id']},
        ),
    ]

# Generated by Django 3.1.5 on 2022-03-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_auto_20220322_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='star',
            field=models.CharField(default=5, max_length=5),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.5 on 2022-03-22 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_auto_20220322_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitedetail',
            name='linked_by',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]

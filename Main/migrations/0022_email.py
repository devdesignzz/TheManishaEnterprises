# Generated by Django 3.1.5 on 2022-03-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0021_auto_20220323_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]

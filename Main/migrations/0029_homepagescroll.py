# Generated by Django 3.1.5 on 2022-04-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0028_auto_20220430_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageScroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Image', models.ImageField(upload_to='pics/banner')),
            ],
        ),
    ]

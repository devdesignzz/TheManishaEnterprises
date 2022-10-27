# Generated by Django 3.1.5 on 2022-03-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_gallery_sqaure_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pics/service')),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2022-03-22 06:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website_Deatil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_first_image', models.ImageField(upload_to='pics/about')),
                ('about_first_detail', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
# Generated by Django 3.1.5 on 2022-03-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_auto_20220322_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_mode',
            field=models.CharField(choices=[('12', 'Landscape'), ('12', 'Portrait')], max_length=2),
        ),
    ]

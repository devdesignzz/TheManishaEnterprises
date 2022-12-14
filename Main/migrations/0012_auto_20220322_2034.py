# Generated by Django 3.1.5 on 2022-03-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0011_project_star'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='finished_data',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project',
        ),
        migrations.RemoveField(
            model_name='project',
            name='star',
        ),
        migrations.RemoveField(
            model_name='project',
            name='started_date',
        ),
        migrations.AddField(
            model_name='project',
            name='image_mode',
            field=models.CharField(choices=[(12, 'Landscape'), (5, 'Portrait')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_heading',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]

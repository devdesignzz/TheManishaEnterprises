# Generated by Django 3.1.5 on 2022-03-22 17:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_auto_20220322_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitedetail',
            name='about_company_footer',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
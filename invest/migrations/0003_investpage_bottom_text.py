# Generated by Django 2.2.9 on 2020-02-04 09:05

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0002_auto_20200204_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='investpage',
            name='bottom_text',
            field=wagtail.core.fields.RichTextField(default='Input here...'),
        ),
    ]

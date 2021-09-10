# Generated by Django 2.2.9 on 2020-02-06 17:08

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqpage',
            name='faqs',
            field=wagtail.core.fields.StreamField([('faq', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('content', wagtail.core.blocks.TextBlock(help_text='Add additional text', required=True))]))], blank=True, null=True),
        ),
    ]
# Generated by Django 2.2.9 on 2020-02-16 06:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0006_auto_20200216_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqpage',
            name='faqs',
            field=wagtail.core.fields.StreamField([('faqs', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('content', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.core.blocks.RichTextBlock())]))]))], blank=True, null=True),
        ),
    ]

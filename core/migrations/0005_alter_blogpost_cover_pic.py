# Generated by Django 5.0.7 on 2024-08-08 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_pic',
            field=models.ImageField(blank=True, null=True, upload_to='blog_posts/cover_pics'),
        ),
    ]

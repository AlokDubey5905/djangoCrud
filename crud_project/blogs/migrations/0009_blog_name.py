# Generated by Django 4.0.3 on 2023-08-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_rename_author_id_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='Anonymous', max_length=30),
            preserve_default=False,
        ),
    ]

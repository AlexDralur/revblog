# Generated by Django 3.2.21 on 2023-11-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_alter_category_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='posts_category', to='forum.Post'),
        ),
    ]

# Generated by Django 3.2.21 on 2023-11-22 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_auto_20231115_2211'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserLike',
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-14 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_category_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]

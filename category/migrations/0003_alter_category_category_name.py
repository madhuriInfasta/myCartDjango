# Generated by Django 4.1.13 on 2024-05-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

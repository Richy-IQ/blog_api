# Generated by Django 5.0.1 on 2024-02-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posters', '0002_remove_category_title_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posters',
            name='category',
            field=models.CharField(choices=[('Science Fiction', 'Science Fiction'), ('Politics', 'Politics'), ('Gist', 'Gist')], default='category', max_length=20),
        ),
    ]

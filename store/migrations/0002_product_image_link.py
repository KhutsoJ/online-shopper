# Generated by Django 5.2 on 2025-05-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.URLField(default='https://placehold.co/600x400/png'),
        ),
    ]

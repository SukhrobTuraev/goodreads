# Generated by Django 4.2.1 on 2023-06-20 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
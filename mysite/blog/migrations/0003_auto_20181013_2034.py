# Generated by Django 2.1.2 on 2018-10-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.FileField(default='default.png', upload_to=''),
        ),
    ]
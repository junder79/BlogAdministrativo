# Generated by Django 2.1.2 on 2018-10-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181013_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='media',
        ),
        migrations.AddField(
            model_name='post',
            name='lala',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]

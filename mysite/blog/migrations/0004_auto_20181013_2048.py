# Generated by Django 2.1.2 on 2018-10-13 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181013_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='media',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_categories_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='img',
            field=models.ImageField(default='notnull', upload_to='Categories'),
        ),
    ]

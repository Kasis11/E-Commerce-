# Generated by Django 4.2.1 on 2023-05-22 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='categoryname',
        ),
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='category'),
        ),
    ]

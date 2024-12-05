# Generated by Django 4.2.1 on 2023-05-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_delete_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='Category')),
            ],
        ),
    ]

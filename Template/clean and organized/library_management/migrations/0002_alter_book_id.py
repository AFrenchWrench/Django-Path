# Generated by Django 5.2.3 on 2025-06-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

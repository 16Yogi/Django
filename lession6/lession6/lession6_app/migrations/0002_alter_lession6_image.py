# Generated by Django 5.1.4 on 2024-12-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lession6_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lession6',
            name='image',
            field=models.ImageField(upload_to='lession/'),
        ),
    ]

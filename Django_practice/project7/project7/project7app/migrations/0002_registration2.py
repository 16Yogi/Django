# Generated by Django 5.1.4 on 2025-01-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project7app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2025-01-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
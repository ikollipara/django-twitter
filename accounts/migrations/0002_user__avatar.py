# Generated by Django 5.0 on 2023-12-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='_avatar',
            field=models.ImageField(blank=True, upload_to='avatars', verbose_name='Avatar'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='audio_file',
            field=models.FileField(upload_to='musics'),
        ),
    ]

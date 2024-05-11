# Generated by Django 5.0.3 on 2024-05-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_album_release_date_alter_album_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together={('title', 'artist')},
        ),
    ]

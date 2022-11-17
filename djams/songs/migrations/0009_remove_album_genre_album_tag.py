# Generated by Django 4.1.3 on 2022-11-17 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0008_rename_artists_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='songs.tag'),
        ),
    ]

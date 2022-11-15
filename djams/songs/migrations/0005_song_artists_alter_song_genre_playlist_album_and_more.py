# Generated by Django 4.1.3 on 2022-11-15 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_alter_artist_grammies_won_alter_song_number_of_plays'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(to='songs.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.genre'),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.genre')),
                ('songs', models.ManyToManyField(to='songs.song')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='songs.genre')),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.album'),
        ),
    ]

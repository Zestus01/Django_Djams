# Generated by Django 4.1.3 on 2022-11-16 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_alter_song_duration_alter_song_number_of_plays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artists',
            new_name='artist',
        ),
    ]

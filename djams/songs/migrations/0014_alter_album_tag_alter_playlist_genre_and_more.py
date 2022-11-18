# Generated by Django 4.1.3 on 2022-11-18 13:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0013_alter_artist_grammies_won'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='songs.tag'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.genre'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.tag'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.genre'),
        ),
        migrations.AlterField(
            model_name='song',
            name='number_of_plays',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

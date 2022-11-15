# Generated by Django 4.1.3 on 2022-11-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('bio', models.TextField(max_length=500)),
                ('monthly_listeners', models.BigIntegerField(default=4200)),
                ('grammies_won', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='songs',
            name='title',
            field=models.CharField(max_length=80),
        ),
    ]

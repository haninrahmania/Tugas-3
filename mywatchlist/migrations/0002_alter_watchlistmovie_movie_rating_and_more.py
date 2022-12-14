# Generated by Django 4.1 on 2022-09-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistmovie',
            name='movie_rating',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='watchlistmovie',
            name='movie_review',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='watchlistmovie',
            name='release_date',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='watchlistmovie',
            name='watched',
            field=models.TextField(default=''),
        ),
    ]

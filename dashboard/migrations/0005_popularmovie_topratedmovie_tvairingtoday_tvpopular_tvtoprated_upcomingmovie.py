# Generated by Django 3.2 on 2022-12-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20221208_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='popularmovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_popular', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='topratedmovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_toprated', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tvairingtoday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tvairingtoday', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tvpopular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tvpopular', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tvtoprated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tvtoprated', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='upcomingmovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_upcoming', models.CharField(blank=True, max_length=100, null=True)),
                ('adult', models.CharField(blank=True, max_length=100, null=True)),
                ('backdrop_path', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('original_language', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('overview', models.TextField()),
                ('popularity', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('vote_count', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

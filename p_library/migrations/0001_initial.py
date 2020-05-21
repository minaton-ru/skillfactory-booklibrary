# Generated by Django 2.2.6 on 2020-05-21 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('copy_count', models.SmallIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
                ('inspirer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inspired_works', to='p_library.Author')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='inspired_authors', through='p_library.Inspiration', to='p_library.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Friend'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Publisher'),
        ),
    ]
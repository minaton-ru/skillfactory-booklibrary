# Generated by Django 2.2.6 on 2020-05-21 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0005_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='p_library.Friend'),
        ),
    ]
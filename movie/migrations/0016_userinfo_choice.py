# Generated by Django 4.0.3 on 2023-11-15 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_remove_userinfo_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.choice'),
        ),
    ]

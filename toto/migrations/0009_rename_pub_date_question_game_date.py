# Generated by Django 4.0.3 on 2023-11-12 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toto', '0008_rename_pub_date_answer_answer_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='game_date',
        ),
    ]

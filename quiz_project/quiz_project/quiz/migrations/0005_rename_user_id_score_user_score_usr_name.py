# Generated by Django 4.1.3 on 2023-12-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_rename_user_score_user_id_score_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='score',
            name='usr_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

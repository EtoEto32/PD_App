# Generated by Django 4.1.3 on 2023-12-11 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

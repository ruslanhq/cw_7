# Generated by Django 2.2 on 2019-10-19 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191019_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='pos_answer',
            new_name='answers',
        ),
    ]

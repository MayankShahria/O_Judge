# Generated by Django 3.2.6 on 2021-09-02 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('online_judge', '0002_submission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_input_file',
            field=models.FileField(default='settings.MEDIA_ROOT/background.gif', storage=django.core.files.storage.FileSystemStorage(location=b'C:/Users/DELL/Documents/OJ/OnlineJudge/media'), upload_to='documents/'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-02 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online_judge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_file', models.FileField(default='background.gif', upload_to='documents/')),
                ('submission_status', models.CharField(max_length=50)),
                ('submission_language', models.CharField(max_length=50)),
                ('submission_time', models.FloatField(default=100.0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_judge.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

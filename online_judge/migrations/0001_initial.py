# Generated by Django 3.2.6 on 2021-09-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(max_length=100)),
                ('question_description', models.CharField(max_length=100000)),
                ('question_input_file', models.CharField(max_length=200)),
                ('question_output_file', models.CharField(max_length=200)),
            ],
        ),
    ]
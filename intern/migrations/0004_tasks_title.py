# Generated by Django 3.2.5 on 2021-07-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0003_tasks_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
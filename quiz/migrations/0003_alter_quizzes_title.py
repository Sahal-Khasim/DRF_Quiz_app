# Generated by Django 3.2.6 on 2021-08-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210811_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='title',
            field=models.CharField(default='New Quiz', max_length=255, verbose_name='Quiz Title'),
        ),
    ]

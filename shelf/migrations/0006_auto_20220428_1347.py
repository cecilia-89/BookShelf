# Generated by Django 3.2.7 on 2022-04-28 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0005_auto_20220428_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='shelf.Category'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-21 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebNovels', '0001_initial'),
    ]

    operations = [

        migrations.AddField(
            model_name='webnovels',
            name='tags',
            field=models.ManyToManyField(blank=True, to='WebNovels.tag'),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-14 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movieactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('horror', 'Horror'), ('fantasy', 'Fantasy'), ('drama', 'Drama'), ('comedy', 'Comedy')], max_length=50),
        ),
    ]

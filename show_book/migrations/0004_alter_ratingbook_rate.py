# Generated by Django 4.1.7 on 2023-02-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_book', '0003_ratingbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingbook',
            name='rate',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '4')], max_length=100, null=True),
        ),
    ]

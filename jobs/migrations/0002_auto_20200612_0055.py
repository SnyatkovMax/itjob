# Generated by Django 3.0.7 on 2020-06-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.PositiveIntegerField(default=500),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]

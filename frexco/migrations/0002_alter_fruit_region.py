# Generated by Django 4.0.1 on 2022-01-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frexco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='frexco.region'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frexco', '0008_alter_region_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(choices=[('S', 'Sul'), ('CO', 'Centro-Oeste'), ('SE', 'Sudeste'), ('NE', 'Nordeste'), ('N', 'Norte')], max_length=2, unique=True),
        ),
    ]

# Generated by Django 3.1 on 2020-08-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_datacsv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datacsv',
            name='nama_bulan',
        ),
        migrations.RemoveField(
            model_name='datacsv',
            name='nama_item',
        ),
        migrations.AlterField(
            model_name='datacsv',
            name='nama_tahun',
            field=models.CharField(max_length=255),
        ),
    ]
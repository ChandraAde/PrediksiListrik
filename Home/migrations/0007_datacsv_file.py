# Generated by Django 3.1 on 2020-08-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200817_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacsv',
            name='file',
            field=models.FileField(default='data.csv', upload_to='media/documents/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-15 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_merge_0005_auto_20220315_1425_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]

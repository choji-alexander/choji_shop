# Generated by Django 2.1 on 2022-10-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choji_products', '0002_choji_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choji_offer',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='choji_offer',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
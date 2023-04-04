# Generated by Django 2.1 on 2022-10-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choji_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choji_offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2083)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
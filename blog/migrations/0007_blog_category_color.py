# Generated by Django 2.0.2 on 2018-11-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181129_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
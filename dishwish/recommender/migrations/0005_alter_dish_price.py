# Generated by Django 4.2.3 on 2023-07-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0004_alter_dish_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.TextField(),
        ),
    ]
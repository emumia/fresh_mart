# Generated by Django 4.2.3 on 2023-07-25 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.CharField(
                choices=[("STOCK IN", "STOCK IN"), ("STOCK OUT", "STOCK OUT")],
                max_length=40,
            ),
        ),
    ]

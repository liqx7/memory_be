# Generated by Django 4.1 on 2022-11-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("memory", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item", name="time_1", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_2", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_3", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_4", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_5", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_6", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_7", field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="item", name="time_8", field=models.DateTimeField(null=True),
        ),
    ]

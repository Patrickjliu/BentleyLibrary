# Generated by Django 4.2.1 on 2023-05-23 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("publisher", models.CharField(max_length=255)),
                ("publication_date", models.DateField()),
                ("isbn", models.CharField(max_length=13)),
                ("borrower_first_name", models.CharField(max_length=255)),
                ("borrower_last_name", models.CharField(max_length=255)),
                ("borrower_email", models.CharField(max_length=255)),
                ("borrowed_date", models.DateField()),
                ("borrowed_time", models.TimeField()),
                ("returned_date", models.DateField(blank=True, null=True)),
                ("returned_time", models.TimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "log",
                "managed": False,
            },
        ),
        migrations.AlterModelOptions(
            name="bookinventory",
            options={"managed": False},
        ),
    ]

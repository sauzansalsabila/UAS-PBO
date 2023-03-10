# Generated by Django 4.1.2 on 2023-01-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_utspbo", "0010_bulan_harga_ikan_rename_nama_latin_lokasi_tpi_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Peta",
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
                ("no", models.IntegerField(null=True)),
                ("nama_lokasi", models.CharField(max_length=50)),
                ("titik_koordinat", models.CharField(max_length=50)),
                ("deskripsi", models.TextField(null=True)),
            ],
        ),
    ]

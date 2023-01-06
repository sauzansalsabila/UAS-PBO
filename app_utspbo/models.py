from distutils.command.upload import upload
from django.db import models

# Create your models here.

class alattangkap(models.Model):
    genre = models.CharField(max_length=50)
    keterangan = models.TextField()
    def __str__(self):
        return self.genre

class lagu(models.Model):
    namakapten = models.CharField(max_length=100)
    jenisikan = models.CharField(max_length=100)
    tanggalberangkat = models.CharField(max_length=100)
    jumlah = models.IntegerField(null=True)
    alattangkap = models.ForeignKey(alattangkap, on_delete=models.CASCADE, null=True)
    img = models.CharField(null=True, max_length=40)
    def __str__(self):
        return self.namakapten

class peta(models.Model):
    koordinat = models.CharField(max_length=100, null=True)
    jumlah = models.CharField(max_length=100, null=True)
    deskripsi = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.koordinat

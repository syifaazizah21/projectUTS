from django.db import models

# Create your models here.
class MataKuliah(models.Model):
    kode_mk = models.CharField(max_length=200)
    nama_mk = models.CharField(max_length=200)
    nama_dosen = models.CharField(max_length=200)
    wp = models.CharField(max_length=200)
    sks = models.CharField(max_length=200)
    deskripsi = models.TextField()

class CatatanMk(models.Model):
    kode_mk = models.CharField(max_length=200)
    nama_mk = models.CharField(max_length=200)
    catatan_mk = models.CharField(max_length=500)

class SoalMk(models.Model):
    kode_mk = models.CharField(max_length=200)
    nama_mk = models.CharField(max_length=200)
    soal_mk = models.CharField(max_length=500)

class Blog(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.CharField(max_length=200)
    penulis = models.CharField(max_length=500)
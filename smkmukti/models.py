from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Agenda(models.Model):
    users           = models.ForeignKey(User,on_delete=models.SET_NULL, null = True)
    agenda_judul    = models.CharField(max_length=255)
    agenda_isi      = models.TextField()
    agenda_date     = models.DateField(null=True,blank=True)
    agenda_time     = models.TimeField(null=True,blank=True)
    
    def __str__(self):
        return "{},{}".format(self.agenda_judul,self.agenda_isi)
        
class Pendaftar(models.Model):
    users           = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    nama_lengkap    = models.CharField(max_length=100)
    email           = models.CharField(max_length=50)
    alamat          = models.TextField()
    no_telp         = models.CharField(max_length=15)
    nama_ayah       = models.CharField(max_length=100)
    nama_ibu        = models.CharField(max_length=100)
    tanggal_daftar  = models.DateField()

    def __str__(self):
        return f"{self.nama_lengkap}, {self.alamat}, {self.no_telp},{nama_ayah}, {self.nama_ibu}, {self.tanggal_daftar}"

class Gallery(models.Model):
    users           = models.ForeignKey(User,on_delete=models.CASCADE)
    judul_gambar    = models.CharField(max_length=255)
    gambar          = models.ImageField()

    def __str__(self):
        return "{},{}".format(self.judul_gambar,self.gambar)

class Kurikulum(models.Model):
    users           = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    judul           = models.CharField(max_length=100)
    gambar          = models.ImageField()

    def __str__(self):
        return f"{self.judul},{self.gambar} "

class DetailKurikulum(models.Model):
    kurikulums      = models.ForeignKey(Kurikulum, on_delete = models.SET_NULL, null = True)
    judul           = models.CharField(max_length=100)
    sub_judul       = models.CharField(max_length=100)
    isi             = models.TextField()

    def __str__(self):
        return f"{self.judul},{self.sub_judul},{self.isi} "

class Pengumuman(models.Model):
    users           = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    judul           = models.CharField(max_length=100)
    isi             = models.TextField()
    tanggal         = models.DateField()

    def __str__(self):
        return f"{self.judul},{self.isi},{self.tanggal} "
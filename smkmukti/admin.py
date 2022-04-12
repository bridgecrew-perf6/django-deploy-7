from django.contrib import admin
from .models import Pendaftar,Agenda,Pengumuman,Kurikulum,DetailKurikulum,Gallery
# Register your models here.

data = [Pendaftar,Agenda,Pengumuman,Kurikulum,DetailKurikulum,Gallery]
admin.site.register(data)
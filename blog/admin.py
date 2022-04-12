from django.contrib import admin
from .models import Blog,GambarBlog,Komentar,Kategori
# Register your models here.
data =[Blog,GambarBlog,Komentar,Kategori]
admin.site.register(data)

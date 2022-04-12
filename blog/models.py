from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import random

# Create your models here.
class Kategori(models.Model):
    kategori            = models.CharField(max_length=50)

    # def __str__(self):
    #     return "id: "+  str(self.id), self.kategori
    def __str__(self):
        return self.kategori

class GambarBlog(models.Model):    
    gambar              = models.ImageField()    
    
    def __str__(self):
        return str(self.gambar)

class Blog(models.Model):
    users               = models.ForeignKey(User,on_delete=models.SET_NULL, null = True)
    kategoris           = models.ForeignKey(Kategori,on_delete=models.SET_NULL, null = True)
    blog_judul          = models.CharField(max_length=100)
    blog_isi            = models.TextField()    
    blog_datetime       = models.DateTimeField()
    gambars             = models.ManyToManyField(GambarBlog, blank = True)
    randomnumber        = models.IntegerField(default=1000000)
    slug                = models.SlugField(max_length=255,blank=True,editable=False) 
    #slug berisikan link dengan tambahan - pada judul hello sehingga link akan menjadi seperti hello-world

    def save(self):  
        self.randomnumber = random.randint(1000,100000000)              
        self.slug = slugify(self.blog_judul)
        super(Blog, self).save()

    # def __str__(self):
    #     return "id: "+  str(self.id),"Judul: " + self.blog_judul
    def __str__(self):
        return self.blog_judul

class Komentar(models.Model):
    blogs                = models.ForeignKey(Blog,on_delete=models.SET_NULL, null = True)
    komentar_nama       = models.CharField(max_length=100) 
    komentar_email      = models.CharField(max_length=100)
    komentar_isi        = models.CharField(max_length=100)
    komentar_datetime   = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return "{},{}".format(self.komentar_nama, self.komentar_datetime)
from django.shortcuts           import render,redirect
from django.views.generic.list  import ListView
from .models                    import Blog,GambarBlog,Komentar,Kategori
from .forms                     import KomentarForm
from django.core.paginator      import Paginator
# Create your views here.

def Index(request):
    blog            = Blog.objects.all()
    kategori        = Kategori.objects.all()    
    terbaru         = Blog.objects.all().order_by('-blog_datetime')[:4]
    blog_paginator  = Paginator(blog,3)
    page_num        = request.GET.get('page')
    page            = blog_paginator.get_page(page_num)
    context={
        'hal':'Blog',
        'count':blog_paginator.count,
        'page':page,
        'berita':blog,
        'kategori':kategori,
        'terbaru':terbaru,
        'nbar':'blog'
    }
    return render(request,'blog/index.html',context)

def FilterBlog(request,data_category):
    kategori        = Kategori.objects.get(kategori = data_category)
    blog            = Blog.objects.filter(kategoris_id=kategori.id)
    terbaru         = Blog.objects.all().order_by('-blog_datetime')[:4]
    blog_paginator  = Paginator(blog,3)
    page_num        = request.GET.get('page')
    page            = blog_paginator.get_page(page_num)
    context={
        'berita':blog,
        'count':blog_paginator.count,
        'page':page,
        'cat':data_category,
        'kategori':Kategori.objects.all(),
        'terbaru':terbaru,
        'nbar':'blog'
    }
    return render(request,'blog/index-filter.html',context)
    
def DetailBlog(request,randomnumber,data_id,data_slug):
    kategori        = Kategori.objects.all()    
    terbaru         = Blog.objects.all().order_by('-blog_datetime')[:4]
    berita          = Blog.objects.get(id=data_id)
    komen           = Komentar.objects.all().filter(blogs=data_id)
    post_form       = KomentarForm(request.POST or None)
    beritaslug      = Blog.objects.get(id=data_id)
    if request.method == 'POST':
        if post_form.is_valid():
            data = post_form.save(commit=False)
            data.blogs=beritaslug
            data.save()
            return redirect('blog:detail' ,randomnumber=beritaslug.randomnumber, data_id=beritaslug.id,data_slug= beritaslug.slug)
    context={
        'post_form':post_form,
        'kategori':kategori,
        'terbaru':terbaru,
        'berita':berita,
        'komen':komen,
        'nbar':'blog'
    }
    return render(request,'blog/blog_detail.html',context)
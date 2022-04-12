from django.shortcuts           import render
from .models                    import Pendaftar,Agenda,Pengumuman,Gallery
from blog.models                import Blog,GambarBlog
from django.views.generic.list  import ListView

class AgendaListView(ListView):
    model=Agenda
    # context_object_name = 'agendas'
    ordering =['agenda_time']
    paginate_by = 2
    queryset = Agenda.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super(AgendaListView, self).get_context_data(**kwargs)
        context['nbar']='agenda'
        return context
    

class PengumumanListView(ListView):
    model=Pengumuman
    # context_object_name = 'pengumumans'
    ordering =['tanggal']
    paginate_by = 3
    queryset = Pengumuman.objects.all()
    def get_context_data(self, **kwargs):
        context = super(PengumumanListView, self).get_context_data(**kwargs)
        context['nbar']='pengumuman'
        return context

def Index(request):
    agenda = Agenda.objects.all().order_by('-agenda_date','-agenda_time')[:4]
    pengumuman = Pengumuman.objects.all().order_by('-tanggal')[:4]
    blog = Blog.objects.all().order_by('-blog_datetime')[:6]    
    context={
        'heading':'Selamat Datang',
        'subheading':'di Smk Mukti Karya Kebumen',
        'hal':'Smk Mukti Karya Kebumen',
        'agenda':agenda,
        'pengumuman':pengumuman,
        'berita':blog,
        'nbar':'home'
    }
    return render(request,'smkmukti/index.html',context)

def Galeri(request):
    galeri = Gallery.objects.all()
    context={
        'hal':'Halaman Galeri',
        'galeri':galeri,
        'nbar':'gallery'
    }
    return render(request,'smkmukti/gallery.html',context)

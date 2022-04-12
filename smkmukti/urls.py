from django.urls import path
from . import views
from .models import Agenda,Pengumuman
from django.conf.urls.static import static
from django.conf import settings

app_name='smkmukti'
urlpatterns = [
    path('',views.Index,name='index'),
    path('agenda/',views.AgendaListView.as_view(template_name='smkmukti/agenda.html'),name='agenda'),
    path('pengumuman/',views.PengumumanListView.as_view(template_name='smkmukti/pengumuman.html'),name='pengumuman'),
    path('gallery/',views.Galeri,name='gallery')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
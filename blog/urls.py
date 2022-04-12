from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name='blog'
urlpatterns = [
    path('',views.Index,name='index'),
    path('category/<data_category>',views.FilterBlog,name='categorytampil'),
    path('detail-blog/<int:randomnumber><int:data_id>/<slug:data_slug>/',views.DetailBlog,name='detail')
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
from django.urls import path

from . import views
from library.settings import DEBUG,STATIC_URL,STATICFILES_DIRS,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
        path('', views.index,name='home'),
        path('upload/', views.upload,name='uploadbooks'),
        path('update/<int:book_id>', views.update_book,name='updatebook'),
        path('delete/<int:book_id>', views.delete_book,name='deletebook'),
       
    ]

if DEBUG:
    urlpatterns+=static(STATIC_URL,document_root=STATICFILES_DIRS)
    urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)
    
    

from django.contrib import admin
from django.urls import path
from resume import views
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name = "home"),
    path('portfolio/', views.portfolio , name = "portfolio"),
    path('blog/', PostListView.as_view() , name = "blog"),
    path('about/', views.about , name = "about"),
    path('contact/', views.contact , name = "contact"),
    
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

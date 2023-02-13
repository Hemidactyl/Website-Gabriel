from . import views
from django.urls import path

urlpatterns = [
    path('', views.AlbumList.as_view(), name='gallery'),
    path('<slug:slug>/', views.AlbumDetail.as_view(), name='album_detail'),
]
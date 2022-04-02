from django.urls import path

from webapp.views import PhotoListView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView, \
    AlbumListView, AlbumDetailView, AlbumCreateView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list_view'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create_view'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update_view'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete_view'),
    path('album/list/', AlbumListView.as_view(), name='album_list_view'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='album_detail_view'),
    path('album/add/', AlbumCreateView.as_view(), name='album_create_view'),

]

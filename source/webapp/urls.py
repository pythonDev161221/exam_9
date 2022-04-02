from django.urls import path

from webapp.views import PhotoListView, PhotoDetailView, PhotoCreateView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='photo_list_view'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail_view'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create_view'),
]

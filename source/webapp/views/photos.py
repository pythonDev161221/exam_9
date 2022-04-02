from django.views.generic import ListView, DetailView

from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/list_view.html'
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/detail_view.html'
    context_object_name = 'photo'

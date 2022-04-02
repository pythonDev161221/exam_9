from django.views.generic import ListView, DetailView

from webapp.models import Album


class AlbumListView(ListView):
    model = Album
    template_name = 'albums/list.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/detail.html'
    context_object_name = 'album'

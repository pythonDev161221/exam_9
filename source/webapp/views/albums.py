from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumListView(ListView):
    model = Album
    template_name = 'albums/list.html'
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/detail.html'
    context_object_name = 'album'


class AlbumCreateView(CreateView):
    model = Album
    template_name = 'albums/create.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:photo_list_view")

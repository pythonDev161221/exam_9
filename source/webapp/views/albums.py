from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    template_name = 'albums/create.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:album_list_view")


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm

    def get_success_url(self):
        return reverse("webapp:album_list_view")


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'

    def get_success_url(self):
        return reverse("webapp:album_list_view")

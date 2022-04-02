from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import Album


class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/list.html'
    context_object_name = 'albums'


class AlbumDetailView(LoginRequiredMixin, DetailView):
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
        return reverse("webapp:photo_list_view")


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    model = Album
    template_name = 'albums/update.html'
    form_class = AlbumForm
    permission_required = 'webapp.change_album'

    def get_success_url(self):
        return reverse("webapp:photo_list_view")

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    permission_required = 'webapp.delete_album'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:photo_list_view")

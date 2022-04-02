from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photos/list_view.html'
    context_object_name = 'photos'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos/detail_view.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/create_view.html'
    form_class = PhotoForm
    print('asef')

    def form_valid(self, form):
        form.instance.author = self.request.user
        self.object = form.save()
        print('valid')
        return super().form_valid()

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = "photos/update_view.html"
    form_class = PhotoForm

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"

    def get_success_url(self):
        return reverse("webapp:photo_list_view")

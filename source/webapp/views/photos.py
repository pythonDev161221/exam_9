from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'photos/list_view.html'
    context_object_name = 'photos'


class PhotoDetailView(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'photos/detail_view.html'
    context_object_name = 'photo'


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photos/create_view.html'
    form_class = PhotoForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = "photos/update_view.html"
    form_class = PhotoForm
    permission_required = 'webapp.change_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = "photos/delete.html"
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


class PhotoAddChoose(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs.get('pk'))
        photo.choose.add(self.request.user)
        return JsonResponse({"choose": f"{photo.choose.count()}", "photo_id": photo.pk})


class PhotoRemoveChoose(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        photo = Photo.objects.get(pk=kwargs.get('pk'))
        photo.choose.remove(self.request.user)
        return JsonResponse({"choose": f"{photo.choose.count()}", "photo_id": photo.pk})
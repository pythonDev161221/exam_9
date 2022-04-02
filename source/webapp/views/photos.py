from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

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


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'photos/create_view.html'
    form_class = PhotoForm
    print('asef')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     self.object = form.save()
    #     print('valid')
    #     return super().form_valid()

    def get_success_url(self):
        return reverse("webapp:photo_list_view")


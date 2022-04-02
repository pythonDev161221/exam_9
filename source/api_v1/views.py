from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api_v1.serializer import PhotoSerializer, UserSerializer
from webapp.models import Photo


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


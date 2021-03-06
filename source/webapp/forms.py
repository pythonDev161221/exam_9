from django import forms

from webapp.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ["author", "private", "choose"]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ["author", "private", "choose"]

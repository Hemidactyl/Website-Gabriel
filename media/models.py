from django.db import models
from django.utils import timezone
from django.forms import ModelChoiceField, ModelForm
from os.path import join as osjoin
from pictures.models import PictureField


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

THUMBNAIL = (
    (0, "No"),
    (1, "Yes")
)

#album model, to collect images into small albums (each album will probably have one video, but let's see about that)
class Album(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    preview = models.ForeignKey('Picture', related_name='preview' , blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#this is to only show the pictures that are related to the currently edited album so that thumbnail can only be chosen from those
class AlbumAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preview'].queryset = Picture.objects.filter(album=self.instance.pk)


#author model, to keep track of the good people whose photos I'm using
class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    website = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)

    def __str__(self):
        return self.name

#picture model, with better picture field
class Picture(models.Model):
    def album_dir_path(self, filename):
        return osjoin('uploads', str(self.album.slug), filename)

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    picture = PictureField(upload_to=album_dir_path)

    def __str__(self):
        return self.title
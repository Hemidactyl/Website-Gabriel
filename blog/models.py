from django.db import models
from os.path import join as osjoin
from pictures.models import PictureField


#blog post model
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATEGORY = (
    (0, "Post"),
    (1, "Fiction"),
    (2, "Chords")
)

LANGUAGE = (
    (0, "English"),
    (1, "Czech")
)

class Post(models.Model):
    def art_dir_path(self, filename):
        return osjoin('uploads', str(self.slug), filename)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    language = models.IntegerField(choices=LANGUAGE, default=0)
    art = PictureField(upload_to=art_dir_path, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
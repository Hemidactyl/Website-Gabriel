from django.views import generic

from .models import Album, Picture

#the list view of all the publushed albums (by status=1)
class AlbumList(generic.ListView):
    queryset = Album.objects.filter(status=1).order_by('-created_on')
    template_name = 'media/album_index.html'

#for viewing all the photos associated with a certain album
class AlbumDetail(generic.DetailView):
    model = Album
    template_name = 'media/album_detail.html'

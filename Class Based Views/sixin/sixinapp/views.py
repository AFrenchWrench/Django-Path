from django.views.generic import ListView, DetailView
from .models import Musician, Album


class MusicianListView(ListView):
    queryset = Musician.objects.all().order_by("name")
    template_name = "musician_list.html"
    paginate_by = 1


class AlbumDetailView(DetailView):
    queryset = Album.objects.filter(num_stars__gte=3)
    model = Album
    template_name = "album_detail.html"

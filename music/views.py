from django.views import generic
from .models import Album

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	# use context_object_name = 'all_albums' or default name object_list

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'
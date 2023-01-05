from django.views.generic import TemplateView, ListView
from bands.models import Band
from musicians.models import Musician
from labels.models import Label
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsListView(ListView):
    context_object_name = 'search_band_results'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET['searching_query']
        return Band.objects.filter(name__icontains=query).order_by('name')
    
    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        query = self.request.GET['searching_query']
        context['search_musician_results'] = Musician.objects.filter(
            Q(name__icontains=query) | Q(full_name__icontains=query)
        ).order_by('name', 'full_name')
        context['search_label_results'] = Label.objects.filter(name__icontains=query).order_by('name')
        return context

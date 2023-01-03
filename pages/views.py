from django.views.generic import TemplateView, ListView
from bands.models import Band
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsListView(ListView):
    model = Band
    context_object_name = 'search_results'
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET['searching_query']
        return Band.objects.filter(
            Q(name__icontains=query) | Q(members__name__icontains=query)
        )

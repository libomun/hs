from django.db.models import Q
from django.views import generic

from .models import News


# News list view
class NewsListView(generic.ListView):
    template_name = 'news/news_list.html'
    queryset = News.objects.filter(is_publish=True).order_by('-published_date')  # ordering by latest published time
    paginate_by = 10  # show Rural360 number in one page


# News detail View
class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'


# News search view
class NewsSearchView(generic.ListView):
    paginate_by = 10
    template_name = 'news/news_search_result.html'

# Return search result
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = News.objects.order_by('-published_date').filter(
                Q(title__icontains=query) | Q(author__icontains=query) | Q(affiliation__icontains=query) | Q(news_content__icontains=query) | Q(published_date__icontains=query)
            )
        return object_list

# Add query content in context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

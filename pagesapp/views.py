from django.views import generic
from .models import Page


class PageIndex(generic.ListView):
    model = Page
    template_name = 'index.html'
    context_object_name = "pages"
    ordering = ['ordering']


class PageDetail(generic.DetailView):
    model = Page
    template_name = 'detail.html'
    context_object_name = "page"


class PageAdd(generic.CreateView):
    model = Page
    fields = ['title', 'content', 'ordering']
    template_name = 'add.html'
    success_url = '/'

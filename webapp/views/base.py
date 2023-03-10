from django.db.models import Q
from django.http import Http404
from django.utils.http import urlencode
from django.views.generic import ListView, RedirectView

from webapp.forms import SearchForm
from webapp.models import Task


class IndexView(ListView):
    template_name = 'tasks/index.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    # def render_to_response(self, context, **response_kwargs):
    #     if not context['tasks']:
    #         raise Http404('Задачи не найдены')
    #     return super().render_to_response(context, **response_kwargs)


class IndexRedirectView(RedirectView):
    pattern_name = 'index'

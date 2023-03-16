from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, RedirectView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = 'projects/projects.html'
    model = Project
    context_object_name = 'projects'

    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)


class ProjectDetailView(DetailView):
    template_name = 'projects/project.html'
    model = Project


class ProjectAddView(LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/project_update.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')


class IndexRedirectView(RedirectView):
    pattern_name = 'projects'

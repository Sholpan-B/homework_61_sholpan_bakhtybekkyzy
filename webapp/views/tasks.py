from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TaskForm
from webapp.models import Task


class TaskDetailView(DetailView):
    template_name = 'tasks/task.html'
    model = Task


class TaskAddView(CreateView):
    template_name = 'tasks/task_add.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    template_name = 'tasks/task_update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'tasks/task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')

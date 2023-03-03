from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, RedirectView

from webapp.forms import TaskForm
from webapp.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'


class TaskDetailView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class TaskAddView(TemplateView):
    template_name = 'task_add.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = TaskForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        status = request.POST.get('status')
        type = request.POST.get('type')
        task = request.POST.get('task')
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_add.html', context={'form': form, 'task': task, 'status': status, 'type': type})


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return render(request, 'task_update.html', context={
            'form': form,
            'task': task
        })


class TaskDeleteView(TemplateView):
    template_name = 'task_confirm_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ConfirmDeleteView(RedirectView):
    def get(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')

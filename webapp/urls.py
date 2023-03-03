from django.urls import path
from webapp.views import TaskAddView, TaskDetailView, TaskUpdateView, TaskDeleteView, ConfirmDeleteView, IndexView, \
    IndexRedirectView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/", IndexRedirectView.as_view(), name='task_index_redirect'),
    path("task/add", TaskAddView.as_view(), name='task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/confirm_delete/', ConfirmDeleteView.as_view(), name='confirm_delete'),
]

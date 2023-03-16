from django.urls import path

from accounts.views import login_view, logout_view
from webapp.views.base import IndexView, IndexRedirectView
from webapp.views.projects import ProjectsView, ProjectAddView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView
from webapp.views.tasks import TaskDetailView, TaskAddView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("task/", IndexRedirectView.as_view(), name='task_index_redirect'),
    path("task/add", TaskAddView.as_view(), name='task_add'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/confirm_delete/', TaskDeleteView.as_view(), name='confirm_delete'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/add/', ProjectAddView.as_view(), name='add_project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/add-task/', TaskAddView.as_view(), name='project_task_add'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('tasks/<int:pk>/confirm-delete-project/', ProjectDeleteView.as_view(), name='confirm_delete_project'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout' )
]

from django.contrib import admin

from webapp.models.statuses import Status
from webapp.models.tasks import Task
from webapp.models.types import Type

# Register your models here.
admin.site.register(Task)
admin.site.register(Type)
admin.site.register(Status)

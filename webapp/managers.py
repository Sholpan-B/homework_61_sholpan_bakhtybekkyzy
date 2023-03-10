from django.db.models import Manager


class TaskManager(Manager):
    def all(self):
        return self.get_queryset().filter(is_deleted=False)

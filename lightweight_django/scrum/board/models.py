from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy

# Create your models here.
class Sprint(models.Model):
    """Development iteration period"""

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)


    def __str__(self):
        return self.name or ugettext_lazy(f'Sprint ending {self.end}')


class Task(models.Model):
    """Unit of work to be done for this sprint"""

    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, ugettext_lazy('Not Started')),
        (STATUS_IN_PROGRESS, ugettext_lazy('In Progress')),
        (STATUS_TESTING, ugettext_lazy('Testing')),
        (STATUS_DONE, ugettext_lazy('Done'))
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, models.CASCADE,blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE,null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


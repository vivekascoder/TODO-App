from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    # ---> Here status indicate weather the task is completed or not.
    #       >True: Completed
    #       >False: Uncompleted(Default)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

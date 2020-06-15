from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50)
    is_completer = models.BooleanField(default=False)

    def __str__(self):
        return self.title
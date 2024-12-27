from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class CreateForum(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    def __str__(self):
        return self.title

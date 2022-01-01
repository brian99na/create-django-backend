from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    title = models.CharField(max_length=24)
    desc = models.TextField(max_length=500)
    file = models.CharField(max_length=1000)
    tags = ArrayField(models.CharField(max_length=400), default=list, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f"{self.title}, {self.desc}"
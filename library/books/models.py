from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    stock = models.PositiveIntegerField()
    summary = models.TextField(blank=True)
    created = models.DateField(auto_now_add=(True))

    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

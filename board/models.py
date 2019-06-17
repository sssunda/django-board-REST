from django.db import models

# Create your models here.
class Posting(models.Model):
    name = models.CharField(max_length=30, blank=False)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False)
    text = models.CharField(max_length=200, blank=False)
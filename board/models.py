from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posting(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        ordering = ['-create_date']
        return self.name + " : " +self.text
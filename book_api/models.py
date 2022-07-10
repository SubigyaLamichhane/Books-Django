from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

#/books/list
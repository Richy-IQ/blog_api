from django.conf import settings
from django.db import models


class Category(models.Model):
      CATEGORY_CHOICES = [
        ('Science Fiction', 'Science Fiction'),
        ('Politics', 'Politics'),
        ('Gist', 'Gist'),
    ]
      category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='category')
    
      def __str__(self) -> str:
         return self.title

class Posters(models.Model):
    CATEGORY_CHOICES = [
        ('Science Fiction', 'Science Fiction'),
        ('Politics', 'Politics'),
        ('Gist', 'Gist'),
    ]
    title = models.CharField(max_length=50)
    body = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='category')
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def comments(self):
        return self.comment_set.all()
  
class Comment(models.Model):
    poster = models.ForeignKey('Posters', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.name} - {self.text}'
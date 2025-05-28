from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    source = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    link = models.URLField(unique=True, max_length=5000)
    description = models.TextField(max_length=5000)
    published = models.DateTimeField()
    author = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.source} - {self.title}'
    
class UserFavoriteArticles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='favorite_articles')
    faved_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'article')
        ordering = ['-faved_at']

    def __str__(self):
        return f'{self.user.username} - {self.article.title}'
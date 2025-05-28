from rest_framework import serializers
from .models import Article, UserFavoriteArticles

class FeedSerializer(serializers.ModelSerializer):
    published = serializers.DateTimeField(format= "%B %d, %Y, %I:%M %p" )

    class Meta: 
        model = Article
        fields = '__all__'


class FavoriteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavoriteArticles
        fields = ['article']
from django.urls import path, include, re_path
from .views import FeedView, FavoritesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'favorites', FavoritesViewSet, basename='favorites')


urlpatterns = [
    path('feeds/', FeedView.as_view(), name='feeds'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    path('feeds/', include(router.urls)),
]

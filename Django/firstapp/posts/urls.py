from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# on utilise le routage par défaut du rest_framework
router = DefaultRouter()
# on définit le chemin de la vue avec le framework rest
router.register('posts', PostViewSet, 'posts')

urlpatterns = [
    path('', include(router.urls)),
]

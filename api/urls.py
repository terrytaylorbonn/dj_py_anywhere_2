from django.urls import path, include
from .views import hello_world
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello/', hello_world, name='hello_world'),
]

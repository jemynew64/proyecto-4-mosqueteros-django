from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
router = DefaultRouter()
router.register(r'notas', NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, NoteViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('note', NoteViewSet, basename='note')  # because there is no queryset a basename is very important

urlpatterns = [
    path('', include(router.urls))
]

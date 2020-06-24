from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recette import views

routers = DefaultRouter()
routers.register('tags', views.TagViewSet)

app_name = 'recette'

urlpatterns = [
    path('', include(routers.urls))
]

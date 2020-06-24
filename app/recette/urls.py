from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recette import views

routers = DefaultRouter()
routers.register('tags', views.TagViewSet)
routers.register('ingredient', views.IngredientViewSet)

app_name = 'recette'

urlpatterns = [
    path('', include(routers.urls))
]

from django.contrib.auth import views
from django.urls import path
from .views import Index, CreateRecipies, CategoryList, RecipesDetail, UpdateRecipes

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add/', CreateRecipies.as_view(), name='add'),
    path('category/<int:pk>', CategoryList.as_view(), name='category'),
    path('recipes/<int:pk>', RecipesDetail.as_view(), name='detail'),
    path('recipes/update/<int:pk>', UpdateRecipes.as_view(), name='update'),
]

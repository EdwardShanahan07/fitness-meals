from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('recipes/', views.RecipeList.as_view(), name="recipes_list"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_like")
]

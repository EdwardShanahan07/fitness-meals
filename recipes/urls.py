from . import views
from django.urls import path

handler404 = views.custom_404

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('recipes/', views.RecipeList.as_view(), name="recipes_list"),
    path('create/', views.RecipeCreate.as_view(), name="recipe_create"),
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('recipe/<slug:slug>/edit/', views.RecipeEdit.as_view(), name="recipe_edit"),
    path('recipe/<slug:slug>/delete/', views.RecipeDelete.as_view(), name="recipe_delete"),
    path('profile/', views.UserProfile.as_view(), name='user_profile'),
    path('like/<slug:slug>/', views.RecipeLike.as_view(), name="recipe_like"),
]

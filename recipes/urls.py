from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('recipes/', views.Recipe_List.as_view(), name="recipes_list")
]

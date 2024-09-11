from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('recipe/', views.recipes_index, name='recipes_index'),
]
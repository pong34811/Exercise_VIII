# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, ),
    path('delete/<anime_id>/', views.delete, name='delete'),
]

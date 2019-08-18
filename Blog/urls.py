from django.urls import path
from . import views

urlpatterns = [
    path('Post/', views.BlogPost, name='BlogPost'),
    path('Edit/<int:pk>', views.BlogEdit, name='BlogEdit'),
    path('', views.Blog, name='Blog'),
]

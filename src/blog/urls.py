from django.urls import path
from .views import index, article, collab_detail

urlpatterns = [
    path('', index, name='blog-index'),
    path('page_01', article, name='blog-article'),
    path('<str:slug>', collab_detail, name='detail'),

]
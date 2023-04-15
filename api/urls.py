from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.controlBlogpost),
    path('posts/<int:id>', views.controlBlogpostId),
]
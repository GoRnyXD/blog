from django.urls import path
from .views import *

urlpatterns = [
    path('profile/<int:pk>', ProfileView, name='profile'),
    path('blog/', BlogView, name='blog'),
    path('detail_blog/<int:pk>', DetailBlogView, name='detail_blog'),
]

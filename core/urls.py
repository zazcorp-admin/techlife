from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='postList'),
    path('post_details/<slug>/', views.post_details, name='postDetails'),
    path('add_blog/', views.add_blog, name='add_blog'),

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post_list/', views.post_list, name='postList'),
    path('post_details/<slug>/', views.post_details, name='postDetails'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<slug>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<slug>/', views.delete_blog, name='delete_blog'),
    path('add_category/',views.add_category, name='addCategory' ),
    path('delete_category/<slug>/', views.delete_category, name='deleteCategory'),
    path('edit_category/<slug>/', views.edit_category, name="editCategory"),
    path('delete_tag/<slug>/', views.delete_tag, name="deleteTag"),
    path('search_result/', views.search_results, name='search_results'),



]

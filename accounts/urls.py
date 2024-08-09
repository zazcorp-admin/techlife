from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
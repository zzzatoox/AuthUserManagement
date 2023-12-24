from django.urls import path
from . import views
from main.views import logout_view

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('create-post', views.create_post, name='create_post'),
]
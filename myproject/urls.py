from django.urls import path
from django.contrib import admin
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('fastfoods/', views.fastfood_list, name='fastfood_list'),
    path('fastfoods/<int:pk>/', views.fastfood_detail, name='fastfood_detail'),
    path('caffeine/', views.caffeine_list, name='caffeine_list'),
    path('caffeine/<int:pk>/', views.caffeine_detail, name='caffeine_detail'),
]

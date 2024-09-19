from django.urls import path
from . import views

# vistas asociadas al front
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # Agrega más rutas según tus necesidades
]

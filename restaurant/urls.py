"""
URL configuration for the restaurant application.
Defines the URL patterns for routing requests to appropriate views.
Includes static and media file serving configurations for development.
"""

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# Paths to each resource/page based on Task 1.1
urlpatterns = [
    #path(r'', views.main, name='main'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('order/', views.order, name='order'),
    path('main/', views.main, name='main'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
""" Added this because a new media route in settings """
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


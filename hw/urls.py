from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.home_page, name="home"),
    path('about/', views.about, name="about"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


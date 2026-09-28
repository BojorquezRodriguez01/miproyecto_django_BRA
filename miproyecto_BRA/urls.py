from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tu_app.urls')),  # Reemplaza 'tu_app' por el nombre de tu aplicación
]
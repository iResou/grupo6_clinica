# mi_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),  # URLs de Usuarios
    path('api/', include('pacientes.urls')),  # URLs de Pacientes
    path('api/', include('citas.urls')),  # URLs de Citas
    path('api/', include('facturacion.urls')),  # URLs de Facturación
    path('api/', include('inventario.urls')),  # URLs de Inventario
    path('api/', include('historias.urls')),  # URLs de Historias Clínicas
]

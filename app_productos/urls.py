from django.urls import path
from . import views

app_name = 'app_productos'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('producto/crear/', views.crear_producto, name='crear_producto'),
    path('producto/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('producto/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
]
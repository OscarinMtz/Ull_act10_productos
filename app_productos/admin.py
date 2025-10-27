from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'activo']
    list_filter = ['categoria', 'activo']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'stock', 'activo']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
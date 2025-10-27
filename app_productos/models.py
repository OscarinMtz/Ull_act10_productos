from django.db import models

class Producto(models.Model):
    CATEGORIAS = [
        ('aceites', 'Aceites Esenciales'),
        ('velas', 'Velas Aromáticas'),
        ('sales', 'Sales de Baño'),
        ('cosmetica', 'Cosmética Natural'),
        ('difusores', 'Difusores'),
        ('otros', 'Otros Productos'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='otros')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']
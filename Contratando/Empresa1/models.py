from django.db import models


# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

# Modelo de Departamento
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre

# Modelo de Puesto
class Puesto(models.Model):
    nombre = models.CharField(max_length=100)
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    departamento = models.ForeignKey(Departamento, related_name='puestos', on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre

# Modelo de Contrato
class Contrato(models.Model):
    empleado = models.ForeignKey(Empleado, related_name='contratos', on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)  # Puede ser null para contratos indefinidos
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    activo = models.BooleanField(default=True)

    def _str_(self):
        return f"Contrato de {self.empleado.nombre} {self.empleado.apellido} en {self.puesto.nombre}"
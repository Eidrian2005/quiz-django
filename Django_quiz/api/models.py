from django.db import models

# Create your models here.

class Ubicacion(models.Model):
    provincia = models.CharField(max_length=255, unique=True)
    ciudad = models.CharField(max_length=255, unique=True)
    calle = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.provincia

class Hotel(models.Model):
    ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE)
    hotel = models.CharField(max_length=255)
    contacto = models.IntegerField(unique=True)

    def __str__(self):
        return self.hotel


class Categoria(models.Model):
    categorias = models.TextField()

    def __str__(self):
        return self.categorias



class Habitaciones(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)   
    numero_habitacion = models.IntegerField(unique=True)

    def __str__(self):
        return  str(self.numero_habitacion)
    

class Clientes(models.Model):
    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre



class Reservas(models.Model):
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    habitaciones = models.ForeignKey(Habitaciones, on_delete=models.CASCADE)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField()
    
    def __str__(self):
        return self.fecha_entrada


class Pagos(models.Model):
    reservas = models.ForeignKey(Reservas, on_delete=models.CASCADE)
    precio = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.precio



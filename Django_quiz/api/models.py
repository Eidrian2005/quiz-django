from django.db import models

# Create your models here.

class Ubicacion(models.Model):
    provincia = models.CharField(max_length=255, unique=True,blank=False)
    ciudad = models.CharField(max_length=255, unique=True, blank=False)
    calle = models.CharField(max_length=255, unique=True, blank=False)

    def __str__(self):
        return self.provincia

class Hotel(models.Model):
    ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE, blank=False)
    hotel = models.CharField(max_length=255 ,blank=False)
    contacto = models.IntegerField(unique=True, blank=False)

    def __str__(self):
        return self.hotel


class Categoria(models.Model):
    categorias = models.TextField()

    def __str__(self):
        return self.categorias



class Habitaciones(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE,blank=False)
    categoria = models.ManyToManyField(Categoria, blank=False)   
    numero_habitacion = models.IntegerField(unique=True,blank=False)

    def __str__(self):
        return  str(self.numero_habitacion)
    

class Clientes(models.Model):
    nombre = models.CharField(max_length=500,blank=False)
    apellido = models.CharField(max_length=100,blank=False)
    direccion = models.CharField(max_length=255,blank=False)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre



class Reservas(models.Model):
    clientes = models.ForeignKey(Clientes,on_delete=models.CASCADE,blank=False)
    habitaciones = models.OneToOneField(Habitaciones, on_delete=models.CASCADE,blank=False)
    fecha_entrada = models.DateTimeField(auto_now_add=True,blank=False)
    fecha_salida = models.DateTimeField(blank=False)
    
    def __str__(self):
        return str( self.fecha_entrada)


class Pagos(models.Model):
    reservas = models.ForeignKey(Reservas, on_delete=models.CASCADE,blank=False)
    precio = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.precio)



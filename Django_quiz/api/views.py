from rest_framework import generics
from .models import Ubicacion,Hotel,Categoria,Habitaciones,Clientes,Reservas,Pagos
from .serializers import UbicacionSerializer,HotelSerializer,CategoriaSerializer,HabitacionesSerializer,ClientesSerializer,ReservasSerializer,PagosSerializer

# Create your views here.

class UbicacionListCreate(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


class UbicacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer



class HotelListCreate(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer



class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class HabitacionesListCreate(generics.ListCreateAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer


class HabitacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer


class ClientesListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class =ClientesSerializer


class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class =ClientesSerializer


class ReservasListCreate(generics.ListCreateAPIView):
    queryset = Reservas.objects.all()
    serializer_class =ReservasSerializer

class ReservasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class =ReservasSerializer
    

class PagosListCreate(generics.ListCreateAPIView):
    queryset = Pagos.objects.all()
    serializer_class =PagosSerializer
    
class PagosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pagos.objects.all()
    serializer_class =PagosSerializer
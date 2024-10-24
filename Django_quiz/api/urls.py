from django.urls import path
from . import views


urlpatterns = [
    path('ubicacion/', views.UbicacionListCreate.as_view(), name='ubicacion-list'),
    path('ubicacion/<int:pk>/', views.UbicacionDetail.as_view(), name='ubicacion-detail'),
    path('hotel/', views.HotelListCreate.as_view(), name='hotel-list'),
    path('hotel/<int:pk>/', views.HotelDetail.as_view(), name='hotel-detail'),
    path('categoria/', views.CategoriaListCreate.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('habitaciones/', views.HabitacionesListCreate.as_view(), name='habitaciones-list'),
    path('habitaciones/<int:pk>/', views.HabitacionesDetail.as_view(), name='habitaciones-detail'),
    path('clientes/', views.ClientesListCreate.as_view(), name='clientes-list'),
    path('clientes/<int:pk>/', views.ClientesDetail.as_view(), name='clientes-detail'),
    path('reservas/', views.ReservasListCreate.as_view(), name='reservas-list'),
    path('reservas/<int:pk>/', views.ReservasDetail.as_view(), name='reservas-detail'),
    path('pagos/', views.PagosListCreate.as_view(), name='pagos-list'),
    path('pagos/<int:pk>/', views.PagosDetail.as_view(), name='pagos-detail'),
]           

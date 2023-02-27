from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('cliente/new/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/list/', views.listar_clientes, name='listar_clientes'),
    path('cliente/edit/<str:dni>/', views.editar_cliente, name="editar_cliente"),
    path('coche/new/', views.agregar_coche, name='agregar_coche'),
    path('coche/list/', views.listar_coches, name='listar_coches'),
    path('coche/edit/<str:matricula>/', views.editar_coche, name="editar_coche"),
    path('alquilar/new/', views.agregar_alquiler, name='agregar_alquiler'),
    path('alquilar/list/', views.listar_alquileres, name='listar_alquileres'),
    path('alquilar/edit/<int:pk>/', views.editar_alquiler, name="editar_alquiler"),
    path('cliente/delete/<str:dni>/', views.borrar_cliente, name="borrar_cliente"),
    path('coche/delete/<str:matricula>/', views.borrar_coche, name="borrar_coche"),
    path('sobre_nosotros', views.sobre_nosotros ,name="sobre_nosotros"),

]

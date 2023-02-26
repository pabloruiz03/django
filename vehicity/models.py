from django.db import models

from django import forms

from django.db import models


class Coche(models.Model):
    matricula = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    tarifa_diaria = models.PositiveIntegerField()


class Cliente(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)


class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dni_cliente = models.CharField(max_length=10)
    matricula_coche = models.CharField(max_length=10)


class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    password = models.CharField(max_length=100)
    confirmacion_password = models.CharField(max_length=100)

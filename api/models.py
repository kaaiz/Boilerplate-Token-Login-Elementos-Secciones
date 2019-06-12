from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=150, default='')

class User(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    username = models.CharField(max_length=50, default='')
    is_staff = models.CharField(max_length=50, default='')
    is_active = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')

class Seccion(models.Model):
    titulo = models.CharField(max_length=50, default='')
    #id_elemento = models.CharField(max_length=50, default='')

class Elemento(models.Model):

    titulo = models.CharField(max_length=50, default='')
    descripcion = models.CharField(max_length=50, default='')
    imagen = models.CharField(max_length=50, default='')
    fecha = models.CharField(max_length=50, default='')
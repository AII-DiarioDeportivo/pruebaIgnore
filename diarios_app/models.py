from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Noticia(models.Model):
    id_noticia = models.IntegerField(unique=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    url_foto = models.URLField()
    url_noticia = models.URLField()
    fecha = models.DateField()
    procedente_de = models.CharField(max_length=25)

    def __unicode__(self):
        return self.titulo

class Usuario(models.Model):
    id_usuario = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Puntuacion(models.Model):
    id_noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __unicode__(self):
        return self.id_noticia + " " + self.id_usuario

class Etiquetas(models.Model):
    id_etiqueta = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)

    noticias = models.ManyToManyField(Noticia)

    def __unicode__(self):
        return self.nombre

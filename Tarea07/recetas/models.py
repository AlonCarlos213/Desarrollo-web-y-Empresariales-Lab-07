from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo 
    
class Comentario(models.Model):  # Aquí estaba el error
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    texto = models.TextField(help_text=u'Tu comentario', verbose_name='Comentario')

    def __str__(self):
        return self.texto

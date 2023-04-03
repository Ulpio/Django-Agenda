from django.db import models
from django.contrib.auth.models import  User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=40,verbose_name="Título")
    descricao = models.TextField(blank=True,null=True,verbose_name="Descrição/Comentário")
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    data_criacao = models.DateTimeField(auto_now=True,verbose_name="Data de Criação")
    localizacao = models.TextField(max_length=50,verbose_name="Localização")
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y | %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

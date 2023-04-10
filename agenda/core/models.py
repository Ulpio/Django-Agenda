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

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

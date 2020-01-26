from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, nome,registro,cpf,funcao,cargo,lotacao, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('O usuário devem ter um endereço de email')

        user = self.model(
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
            nome=nome,
            registro=registro,
            cpf=cpf,
            funcao=funcao,
            cargo=cargo,
            lotacao=lotacao,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome,registro,cpf,funcao,cargo,lotacao, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            nome=nome,
            registro=registro,
            cpf=cpf,
            funcao=funcao,
            cargo=cargo,
            lotacao=lotacao,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nome = models.CharField(max_length=120, null=False, blank=False)
    registro = models.CharField(max_length=11, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    funcao = models.CharField(max_length=35, null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    lotacao = models.CharField(max_length=35, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','regsitro']

    def __str__(self):
        return self.nome

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



# class User(AbstractUser):
#     nome = models.CharField(max_length=120, null=False, blank=False)
#     registro = models.CharField(max_length=11, null=True, blank=True)
#     email = models.EmailField(null=False, blank=False)
#     funcao = models.CharField(max_length=35, null=True, blank=True)
#     cargo = models.CharField(max_length=50, null=True, blank=True)
#     lotacao = models.CharField(max_length=35, null=True, blank=True)

# Create your models here.
from django.utils import timezone


class Tipo(models.Model):

    titulo = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.titulo


class Data(models.Model):
    dia = models.DateField(null=False, blank=False)
    inicio = models.TimeField(null=False, blank=False)
    fim = models.TimeField(null=False, blank=False)


# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
#     registro = models.CharField(max_length=11)
#     funcao = models.CharField(max_length=35, null=True, blank=True)
#     cargo = models.CharField(max_length=50, null=True, blank=True)
#     lotacao = models.CharField(max_length=35, null=True, blank=True)


class Reuniao(models.Model):
    COR_CHOICES = (
        ("1", "#5C63DE"),
        ("2", "#CEC02D"),
        ("3", "#81CE2D"),
        ("4", "#2DCEB7"),
    )
    STATUS_CHOICES = (
        ("1", "Agendada"),
        ("2", "Confirmada"),
        ("3", "Consolidada"),
        ("4", "Cancelada"),
    )
    tipo_reuniao = models.ForeignKey('Tipo', on_delete=models.CASCADE)
    data_reuniao = models.ForeignKey('Data', on_delete=models.CASCADE)
    pauta = models.CharField(max_length=120, null=False, blank=False)
    local = models.CharField(max_length=120, null=False, blank=False)
    semestre = models.CharField(max_length=6, null=False, blank=False)
    participantes = models.ManyToManyField(User)
    observacoes = models.TextField(null=True, blank=True)
    deliberacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)
    cor = models.CharField(max_length=1, choices=COR_CHOICES,default="1", null=False, blank=False)

class Alerta(models.Model):
    STATUS_CHOICES = (
        ("1", "Novo"),
        ("2", "Visualizado"),
    )
    titulo = models.CharField(max_length=120, null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)

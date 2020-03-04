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
    registro = models.CharField(max_length=11, null=False, blank=False, unique=True)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    funcao = models.CharField(max_length=35, null=True, blank=True)
    cargo = models.CharField(max_length=50,null=False, blank=False)
    lotacao = models.CharField(max_length=35,null=False, blank=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome','regsitro', 'cpf', 'cargo', 'lotacao']


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

class Tipo(models.Model):
    titulo = models.CharField(max_length=120, null=False, blank=False, unique=True)

    def __str__(self):
        return self.titulo


class Data(models.Model):
    dia = models.DateField(null=False, blank=False)
    inicio = models.TimeField(null=False, blank=False)
    fim = models.TimeField(null=False, blank=False)



class Reuniao(models.Model):
    COR_CHOICES = (
        ("1", "#FFF176"),
        ("2", "#4CAF50"),
        ("3", "#78909C"),
        ("4", "#FF5722"),
    )
    STATUS_CHOICES = (
        ("1", "Agendada"),
        ("2", "Confirmada"),
        ("3", "Consolidada"),
        ("4", "Cancelada"),
    )
    tipo_reuniao = models.ForeignKey('Tipo', on_delete=models.CASCADE)
    data_reuniao = models.ForeignKey('Data', on_delete=models.CASCADE)
    pauta = models.CharField(max_length=255, null=False, blank=False)
    presidente = models.CharField(max_length=120, null=True, blank=True)
    local = models.CharField(max_length=120, null=False, blank=False)
    semestre = models.CharField(max_length=6, null=False, blank=False)
    participantes = models.ManyToManyField(User)
    observacoes = models.TextField(null=True, blank=True)
    deliberacoes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)
    cor = models.CharField(max_length=1, choices=COR_CHOICES,default="1", null=False, blank=False)
    def __str__(self):
        return self.pauta


class Alerta(models.Model):
    STATUS_CHOICES = (
        ("1", "Novo"),
        ("2", "Visualizado"),
    )
    titulo = models.CharField(max_length=120, null=False, blank=False)
    informacoes = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1", null=False, blank=False)


class Departamentos(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    chefia = models.ForeignKey('User', on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

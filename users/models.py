from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)
    cpf = models.IntegerField()
    data_nascimento = models.DateField()

    setTipe = (
        (1, '1'),
    )
    tipo = models.IntegerField(choices=setTipe, default=1)

    def up_img(instance, filename):
        return f"users/{instance.id}-{instance.first_name}.jpeg"

    imagem = models.ImageField(upload_to=up_img, blank=True)

    Oftamo = 'Oftamo'
    Urolo = 'Urolo'
    Cardio = 'Cardio'
    Pedia = 'Pedia'
    Enf = 'Enf'
    Aux = 'Aux'
    Pac = 'Paciente'

    setEspec = (
        (Oftamo, 'Oftamologista'),
        (Urolo, 'Urologista'),
        (Cardio, 'Cardiologista'),
        (Pedia, 'Pediatra'),
        (Enf, 'Enfermeiro(a)'),
        (Aux, 'Auxiliar'),
        (Pac, 'Paciente'),
    )

    especialidade = models.CharField(max_length=20, choices=setEspec, default=Pac)
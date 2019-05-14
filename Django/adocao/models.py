from django.db import models


class Pessoa(models.Model):

    Funcionario = 'FC'
    Colaborador = 'CL'
    GestorDeFazenda = 'GF'
    Veterinario = 'VT'
    Proprietario = 'PT'
    Tipo_Pessoa_Categoria = (
        (Funcionario, 'Funcionario'),
        (Colaborador, 'Colaborador'),
        (Veterinario, 'Veterinario'),
        (Proprietario, 'Proprietario'),
        (GestorDeFazenda, 'GestorDeFazenda')
    )
    categoria = models.CharField(
        max_length=100,
        choices=Tipo_Pessoa_Categoria,
        default=Funcionario,
    )

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    rg = models.IntegerField(
        max_length=11,
        null=False,
        blank=False
    )
    cpf = models.IntegerField(
        max_length=14,
        null=False,
        blank=False
    )
    telefone = models.IntegerField(
        max_length=12,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    cidade = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    bairro = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    cep = models.IntegerField(
        max_length=8,
        null=False,
        blank=False
    )
    uf = models.CharField(
        max_length=2,
        null=False,
        blank=False
    )


#  FIM DA CLASSE PESSOA


class Fazenda(models.Model):

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

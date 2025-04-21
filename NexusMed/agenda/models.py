from django.db import models

class Paciente(models.Model):
    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['nome']


class Atendimento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.titulo} - {self.paciente.nome}'

    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering = ['data_inicio']
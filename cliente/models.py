from django.db import models

# Create your models here.

class Caregoria(models.Model):
    nome = models.CharField(max_length = 100)
class Transacao(models.Model):
    data = models.DateField(auto_now_add = True)
    descricao = models.CharField(max_length = 300)
    valor = models.DecimalField(max_digits= 7, decimal_places= 2)
    catergoria = models.ForeignKey(Caregoria, on_delete = models.CASCADE)

class Evento(models.Model):
	data  = models.DateTimeField()
	tema = models.CharField(max_length = 100)
	descricao  = models.CharField(max_length = 500)
	local = models.CharField(max_length = 120)
	Caregoria = models.ForeignKey(Caregoria, on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'Evento'
	def __str__(self):
		return self.descricao

class Funcionario(models.Model):
	nome = models.CharField(max_length = 250)
	dataNasc = models.DateTimeField()
	cargo = models.CharField(max_length = 150)
	salario = models.DecimalField(max_digits = 7,decimal_places = 2)
	class Meta:
		verbose_name_plural = 'Funcionário'
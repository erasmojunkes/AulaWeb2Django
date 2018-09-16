from django.db import models

# Create your models here.

class Caregoria(models.Model):
    nome = models.CharField(max_length = 100)
class Transacao(models.Model):
    data = models.DateField(auto_now_add = True)
    descricao = models.CharField(max_length = 300)
    valor = models.DecimalField(max_digits= 7, decimal_places= 2)
    catergoria = models.ForeignKey(Caregoria, on_delete = models.CASCADE)
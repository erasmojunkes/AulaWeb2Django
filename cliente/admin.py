from django.contrib import admin
from .models import Caregoria
from .models import Transacao
from .models import Evento
from .models import Funcionario

# Register your models here.

admin.site.register(Caregoria)
admin.site.register(Transacao)
admin.site.register(Evento)
admin.site.register(Funcionario)
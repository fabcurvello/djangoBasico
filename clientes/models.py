from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    email = models.EmailField('E-mail', max_length=40)
    nascimento = models.DateField('Data de Nascimento')
    def __str__(self):
        return self.nome




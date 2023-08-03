from django.db import models

# Create your models here.

class Produto(models.Model):
    nomenclatura = models.CharField('Nomenclatura', max_length=50, unique=True)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em Estoque')


'''
    Criar a classe com o nome desejado para a TAbela no BD. Argumento vem de models.Model.

    Cada atributo será uma coluna da tabela. Estes atributos são tipados de acordo com o método apontado 
    (ex: models.IntegerField para int.)

    Nesses métodos de tipagem, o primeiro argumento é um label. Se for necessário mais alguma característica, 
    pode passar (ex: max_length para definir o máximo de caracteres)
'''
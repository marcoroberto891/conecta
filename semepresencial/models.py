from django.db import models

# Create your models here.


##ABSTRAÇAO
class Pessoa():

    ##__init__ E O CONSTRUTOR , OU  MELHOR O INICIALIZADOR
    def __init__(self,nome ,idade):

    ##self e o 1° parametro formal em todos os metodos de instancia
    def __str__(self):
        return self.nome

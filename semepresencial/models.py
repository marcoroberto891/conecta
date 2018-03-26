from django.db import models


class Pessoa():
    nome = ''
    data_nascimento = None

    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

        def __str__(self):
            return self.nome

    ##HERANÇA
class PessoaFisica(Pessoa):
        def __init__(self, cpf):
            self.cpf = cpf

        def __str__(self):
            return u'{} - {}'.format(self.cpf, self.nome)

   ##ENCAPSULAMENTO


    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

from django.db import models


class User(models.Model):
    login = models.CharField('login',max_length=100)
    senha = models.CharField('senha',max_length=6)

    ##HERANÇA


class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=150)
    usuario = models.CharField(User, related_name='users_admin', null=True,blank=False)
    ## self.endereco = Endereco('rua 1')  ##COMPOSICAO

    def __init__(self, nome, email, usuario):  ##POLIMORFISMO
        self.nome = nome
        self.email = email
        self.usuario = usuario

    def __str__(self):
        return self.nome


class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=12)

    def __init__(self, nome, email, usuario):  ##POLIMORFISMO
        Pessoa.__init__(self, nome, email, usuario)


    def __str__(self):
        return self.cpf


class PessoaJuridica(Pessoa):
        cnpj = None

        def __init__(self, nome, email, usuario, cnpj):  ##POLIMORFISMO
            Pessoa.__init__(self, nome, email, usuario)
            self.cnpj = cnpj


    ##ENCAPSULAMENTO
class Produto():
    nome= ''
    descricao= None
    validade = None

    def __init__(self, nome, descricao, validade):
        self.nome = nome
        self.descricao = descricao
        self.validade = validade

    def __str__(self):
        return self.nome

from django.contrib import admin
from semepresencial.models import Pessoa, PessoaFisica, PessoaJuridica, Produto
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Produto)
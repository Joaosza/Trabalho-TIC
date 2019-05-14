from django.shortcuts import render

from django.views.generic import TemplateView
# Importa tudo que tem em models.py
from .models import *
#  importar um método para redirecionar o usuário depois de efetuar o cadastro
from django.urls import reverse_lazy 
# importar o método que utilizaremos como “Pai” para nossas telas de cadastro:
from django.views.generic.edit import CreateView


# Cria uma classe com herança de TemplateView para exibir
# um arquivo HTML normal (com o conteúdo dele)
class PaginaInicialView(TemplateView):
    # Nome do arquivo que vai ser utilizado para renderizar
    # esta página/método/classe
    template_name = "index.html"

# Página "Sobre"
class SobreView(TemplateView):
    template_name = "sobre.html"

# Página "Cadastro"
class CadastroView(TemplateView):
    template_name = "cadastro.html"

# Página "Cadastro"
class ContatoView(TemplateView):
    template_name = "contato.html"

#Página do Curriculo
class CurriculoView(TemplateView):
    template_name = "curriculo.html"

#Página de Login
class LoginView(TemplateView):
    template_name = "login.html"

#Página de Cadastro
class cadastroUsuarioView(TemplateView):
    template_name = "cadastroUsuario.html"

#Página de dash
class dashView(TemplateView):
    template_name = "dashboard.html"

#Página Base
class baseView(TemplateView):
    template_name = "base.html"

# Cadastro Pessoa
class cadastroPessoaView(TemplateView):
    template_name = "cadastroPessoa.html"

class formView(TemplateView):
    template_name = "form.html"




class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome']
    fields = ['rg']
    fields = ['cpf']
    fields = ['telefone']
    fields = ['email']
    fields = ['cidade']
    fields = ['bairro']
    fields = ['cep']
    fields = ['uf']
    template_name = 'form.html'
    success_url = reverse_lazy('index')


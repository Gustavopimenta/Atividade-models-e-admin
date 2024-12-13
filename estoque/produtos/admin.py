from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'quantidade_estoque', 'data_criacao')
    search_fields = ('codigo', 'nome')
    list_filter = ('data_criacao',)
    ordering = ('-data_criacao',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')

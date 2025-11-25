from django.contrib import admin
from .models import Produto

# Isso configura a listagem bonita na gerência
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'preco', 'disponivel') # Colunas que aparecem na lista
    list_filter = ('marca', 'disponivel') # Filtros laterais
    search_fields = ('nome', 'marca') # Barra de busca
    list_editable = ('preco', 'disponivel') # Permite editar preço rápido sem abrir o produto

# Registra o modelo
admin.site.register(Produto, ProdutoAdmin)
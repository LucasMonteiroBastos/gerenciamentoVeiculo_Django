from django.contrib import admin
from .models import Veiculo,Marca,Proprietario,Contact
admin.site.register(Contact)

@admin.register(Veiculo)
class AdminVeiculo(admin.ModelAdmin):
    # colunas no admin
    list_display = ('marca','modelo','proprietario', 'preco')
    # colunas clicáveis
    list_display_links = ('marca','modelo','proprietario', 'preco')
    # Filtro da lista
    list_filter = ('proprietario','marca')
    # pesquisa nos campos informados
    search_fields = ('marca__nome','modelo','proprietario__cpf')


admin.site.register(Marca)
admin.site.register(Proprietario)
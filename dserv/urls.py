"""Configuração de URL para o aplicativo dserv"""
from django.urls import path
from . import views

app_name = 'dserv'
urlpatterns = [
    #Página inicial
    path('', views.index, name='index'),
    path('em-andamento/', views.ordens_em_andamento, name='ordens_em_andamento'),
    path('editar-ordem/<int:ordem_id>/', views.editar_ordem, name='editar_ordem'),
    path('concluidas/', views.ordens_concluidas, name='ordens_concluidas'),
    path('cadastrar-ordem/', views.cadastrar_ordem, name='cadastrar_ordem'),
    path('relatorio-blocos/', views.relatorio_blocos, name='relatorio_blocos'),
    path('pagamento/<int:mes_pgto_id>/', views.relatorio_pagamento, name='relatorio_pagamento'),
    path('relatorio-pagamento/<int:mes_pgto_id>/exportar-csv/', views.exportar_relatorio_pagamento_csv, name='exportar_relatorio_pagamento_csv'),
    path('meses-pagamento/', views.listar_meses_pagamento, name='listar_meses_pagamento'),
]

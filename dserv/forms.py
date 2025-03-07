"""Formulários para o aplicativo dserv"""
from django.forms import ModelForm, inlineformset_factory, Form, ModelChoiceField
from .models import OrdemDeServico, EmpenhoUtilizado, ManutencaoBloco, MesPagamento

class OrdemDeServicoForm(ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = ['numero', 'ano', 'processo', 'prazo', 'data_emissao', 'data_conclusao', 'fiscal', 'categoria', 'situacao', 'mespgto', 'descricao']

class EmpenhoUtilizadoForm(ModelForm):
    class Meta:
        model = EmpenhoUtilizado
        fields = ['empenho', 'valor_utilizado']

class ManutencaoBlocoForm(ModelForm):
    class Meta:
        model = ManutencaoBloco
        fields = ['bloco', 'valor_bloco', 'ambiente']

# Formsets para os relacionamentos
EmpenhoUtilizadoFormSet = inlineformset_factory(
    OrdemDeServico,  # Modelo principal
    EmpenhoUtilizado,  # Modelo relacionado
    form=EmpenhoUtilizadoForm,  # Formulário usado
    extra=1,  # Número de formulários extras exibidos
    can_delete=True,  # Permite excluir registros
)

ManutencaoBlocoFormSet = inlineformset_factory(
    OrdemDeServico,  # Modelo principal
    ManutencaoBloco,  # Modelo relacionado
    form=ManutencaoBlocoForm,  # Formulário usado
    extra=1,  # Número de formulários extras exibidos
    can_delete=True,  # Permite excluir registros
)

class FiltroMesPagamentoForm(Form):
    mes_pagamento = ModelChoiceField(
        queryset=MesPagamento.objects.all(),
        label="Mês de Pagamento",
        required=False,  # Permite que o filtro seja opcional
    )

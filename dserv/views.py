import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count, Q, F
from django.contrib import messages
from decimal import Decimal
from django.contrib.auth.decorators import login_required, permission_required

from .models import OrdemDeServico, EmpenhoUtilizado, Categoria, Fiscal, MesPagamento, Empenho, Situacao, Bloco, ManutencaoBloco
from .forms import OrdemDeServicoForm, EmpenhoUtilizadoFormSet, ManutencaoBlocoFormSet, FiltroMesPagamentoForm

def index(request):
    """Página inicial mostra resumo das informações"""
    # Quantidade de ordens cadastradas
    total_ordens = OrdemDeServico.objects.count()

    # Quantidade de ordens por tipo de categoria
    ordens_por_categoria = OrdemDeServico.objects.values('categoria__categoria').annotate(total=Count('id'))

    # Quantidade de ordens atribuídas para cada fiscal
    ordens_por_fiscal = OrdemDeServico.objects.values('fiscal__nome_fiscal').annotate(total=Count('id'))

    # Lista dos meses de pagamento cadastrados e valor concluído em cada mês
    # Filtra apenas as ordens com situação "CONCLUIDO"
    situacao_concluido = Situacao.objects.get(situacao="CONCLUIDO")
    meses_pagamento = MesPagamento.objects.annotate(
        total_concluido=Sum(
            'ordemdeservico__empenhos_utilizados__valor_utilizado',
            filter=Q(ordemdeservico__situacao=situacao_concluido)
        )
    ).order_by('id')

    # Valor total utilizado para cada empenho cadastrado, valor empenhado e saldo atual do empenho
    empenhos_info = Empenho.objects.annotate(
        total_utilizado=Sum('empenhoutilizado__valor_utilizado')
    ).values('numero_emp', 'valor_emp', 'total_utilizado')

    for empenho in empenhos_info:
        # Define total_utilizado como 0.00 se for None
        total_utilizado = empenho['total_utilizado'] or Decimal('0.00')
        empenho['saldo'] = empenho['valor_emp'] - total_utilizado

    context = {
        'total_ordens': total_ordens,
        'ordens_por_categoria': ordens_por_categoria,
        'ordens_por_fiscal': ordens_por_fiscal,
        'meses_pagamento': meses_pagamento,
        'empenhos_info': empenhos_info,
    }

    return render(request, 'dserv/index.html', context)

@login_required
def ordens_em_andamento(request):
    # Obtém a situação "EM ANDAMENTO"
    situacao_em_andamento = Situacao.objects.get(situacao="EM ANDAMENTO")

    # Filtra os meses de pagamento que possuem pelo menos uma ordem em andamento
    meses_pagamento = MesPagamento.objects.annotate(
        total_ordens=Count('ordemdeservico', filter=Q(ordemdeservico__situacao=situacao_em_andamento))
    ).filter(total_ordens__gt=0).prefetch_related(
        'ordemdeservico_set'
    )

    # Filtra as ordens em andamento para cada mês de pagamento
    for mes in meses_pagamento:
        mes.ordens_em_andamento = mes.ordemdeservico_set.filter(situacao=situacao_em_andamento)

    context = {
        'meses_pagamento': meses_pagamento,
    }
    return render(request, 'dserv/ordens_em_andamento.html', context)

@login_required
@permission_required('dserv.editar_ordem', raise_exception=True)   
def editar_ordem(request, ordem_id):
    ordem = get_object_or_404(OrdemDeServico, id=ordem_id)

    if request.method == 'POST':
        form = OrdemDeServicoForm(request.POST, instance=ordem)
        empenho_formset = EmpenhoUtilizadoFormSet(request.POST, instance=ordem)
        bloco_formset = ManutencaoBlocoFormSet(request.POST, instance=ordem)

        if form.is_valid() and empenho_formset.is_valid() and bloco_formset.is_valid():
            form.save()
            empenho_formset.save()
            bloco_formset.save()
            # Adiciona a mensagem de sucesso
            messages.success(request, 'Ordem de serviço atualizada!')
            return redirect('dserv:editar_ordem', ordem_id=ordem.id)  # Redireciona para a ordem editada
    else:
        form = OrdemDeServicoForm(instance=ordem)
        empenho_formset = EmpenhoUtilizadoFormSet(instance=ordem)
        bloco_formset = ManutencaoBlocoFormSet(instance=ordem)

    context = {
        'form': form,
        'empenho_formset': empenho_formset,
        'bloco_formset': bloco_formset,
        'ordem': ordem,
    }
    return render(request, 'dserv/editar_ordem.html', context)

@login_required
def ordens_concluidas(request):
    # Obtém a situação "CONCLUIDO"
    situacao_concluido = Situacao.objects.get(situacao="CONCLUIDO")

    # Filtra os meses de pagamento que possuem pelo menos uma ordem concluída
    meses_pagamento = MesPagamento.objects.annotate(
        total_ordens=Count('ordemdeservico', filter=Q(ordemdeservico__situacao=situacao_concluido))
    ).filter(total_ordens__gt=0).prefetch_related(
        'ordemdeservico_set'
    )

    # Formulário de filtro
    filtro_form = FiltroMesPagamentoForm(request.GET or None)

    # Aplica o filtro se o formulário for válido
    if filtro_form.is_valid():
        mes_pagamento = filtro_form.cleaned_data.get('mes_pagamento')
        if mes_pagamento:
            meses_pagamento = meses_pagamento.filter(id=mes_pagamento.id)

    # Filtra as ordens concluídas para cada mês de pagamento
    for mes in meses_pagamento:
        mes.ordens_concluidas = mes.ordemdeservico_set.filter(situacao=situacao_concluido)

    context = {
        'meses_pagamento': meses_pagamento,
        'filtro_form': filtro_form,
    }
    return render(request, 'dserv/ordens_concluidas.html', context)

@login_required
@permission_required('dserv.cadastrar_ordem', raise_exception=True)
def cadastrar_ordem(request):
    if request.method == 'POST':
        form = OrdemDeServicoForm(request.POST)
        empenho_formset = EmpenhoUtilizadoFormSet(request.POST)
        bloco_formset = ManutencaoBlocoFormSet(request.POST)

        if form.is_valid() and empenho_formset.is_valid() and bloco_formset.is_valid():
            ordem = form.save()  # Salva a ordem de serviço
            empenho_formset.instance = ordem
            empenho_formset.save()  # Salva os empenhos utilizados
            bloco_formset.instance = ordem
            bloco_formset.save()  # Salva os blocos associados

            messages.success(request, 'Ordem de serviço cadastrada com sucesso!')
            return redirect('dserv:editar_ordem', ordem_id=ordem.id)  # Redireciona para a lista de ordens
    else:
        form = OrdemDeServicoForm()
        empenho_formset = EmpenhoUtilizadoFormSet()
        bloco_formset = ManutencaoBlocoFormSet()

    context = {
        'form': form,
        'empenho_formset': empenho_formset,
        'bloco_formset': bloco_formset,
    }
    return render(request, 'dserv/cadastrar_ordem.html', context)

@login_required
def relatorio_blocos(request):
    # Calcula a soma dos valores por bloco e obtém as ordens de serviço associadas
    blocos = Bloco.objects.annotate(
        total_gasto=Sum('manutencaobloco__valor_bloco')
    ).prefetch_related(
        'manutencaobloco__ordem'  # Prefetch para as ordens de serviço associadas
    ).values('nome_bloco', 'total_gasto')

    # Para cada bloco, adiciona as informações das ordens de serviço associadas
    blocos_com_ordens = []
    for bloco in blocos:
        ordens = ManutencaoBloco.objects.filter(bloco__nome_bloco=bloco['nome_bloco']).select_related('ordem')
        ordens_info = []
        for ordem in ordens:
            ordens_info.append({
                'numero': ordem.ordem.numero,
                'ano': ordem.ordem.ano,
                'data_emissao': ordem.ordem.data_emissao,
                'data_conclusao': ordem.ordem.data_conclusao,
                'valor_bloco': ordem.valor_bloco,
            })
        blocos_com_ordens.append({
            'nome_bloco': bloco['nome_bloco'],
            'total_gasto': bloco['total_gasto'],
            'ordens': ordens_info,
        })

    context = {
        'blocos': blocos_com_ordens,
    }
    return render(request, 'dserv/relatorio_blocos.html', context)

@login_required
def relatorio_pagamento(request, mes_pgto_id):
    # Obtém o mês de pagamento específico
    mes_pgto = get_object_or_404(MesPagamento, id=mes_pgto_id)

    # Filtra as ordens concluídas no mês de pagamento específico
    ordens_concluidas = OrdemDeServico.objects.filter(
        mespgto=mes_pgto,
        situacao__situacao="CONCLUIDO"  # Certifique-se de que "CONCLUIDO" existe no banco
    )

    # Quantidade de ordens cadastradas no mês de pagamento específico
    total_ordens_mes = ordens_concluidas.count()

    # Valor total das ordens no mês de pagamento específico
    valor_total_mes = ordens_concluidas.aggregate(
        total=Sum('empenhos_utilizados__valor_utilizado')
    )['total'] or 0.00

    # Quantidade de ordens por tipo de categoria no mês de pagamento específico
    ordens_por_categoria_mes = ordens_concluidas.values(
        'categoria__categoria'
    ).annotate(
        total=Count('id')
    )

    # Quantidade de ordens atribuídas para cada fiscal no mês de pagamento específico
    ordens_por_fiscal_mes = ordens_concluidas.values(
        'fiscal__nome_fiscal'
    ).annotate(
        total=Count('id')
    )

    # Lista das ordens de serviço concluídas no mês de pagamento específico
    ordens_detalhadas = ordens_concluidas.annotate(
        valor_total=Sum('empenhos_utilizados__valor_utilizado')
    ).values(
        'numero', 'ano', 'processo', 'fiscal__nome_fiscal', 'valor_total', 'descricao'
    )

    # Valor total utilizado para cada empenho cadastrado no mês de pagamento específico
    # Filtra apenas os empenhos utilizados em ordens concluídas
    empenhos_info_mes = EmpenhoUtilizado.objects.filter(
        ordem__mespgto=mes_pgto,
        ordem__situacao__situacao="CONCLUIDO"  # Filtra apenas ordens concluídas
    ).values(
        'empenho__numero_emp'
    ).annotate(
        total_utilizado=Sum('valor_utilizado')
    )

    context = {
        'mes_pgto': mes_pgto,
        'total_ordens_mes': total_ordens_mes,
        'valor_total_mes': valor_total_mes,
        'ordens_por_categoria_mes': ordens_por_categoria_mes,
        'ordens_por_fiscal_mes': ordens_por_fiscal_mes,
        'ordens_detalhadas': ordens_detalhadas,
        'empenhos_info_mes': empenhos_info_mes,
    }
    return render(request, 'dserv/relatorio_pagamento.html', context)

@login_required
@permission_required('dserv.exportar_relatorio', raise_exception=True)
def exportar_relatorio_pagamento_csv(request, mes_pgto_id):
    # Obtém o mês de pagamento específico
    mes_pgto = get_object_or_404(MesPagamento, id=mes_pgto_id)

    # Filtra as ordens concluídas no mês de pagamento específico e calcula o valor total
    ordens_concluidas = OrdemDeServico.objects.filter(
        mespgto=mes_pgto,
        situacao__situacao="CONCLUIDO"
    ).annotate(
        valor_total=Sum('empenhos_utilizados__valor_utilizado')
    ).values(
        'numero', 'ano', 'processo', 'fiscal__nome_fiscal', 'data_emissao', 'data_conclusao', 'valor_total', 'descricao'
    )

    # Cria a resposta HTTP com o tipo de conteúdo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="relatorio_pagamento_{mes_pgto.mes_pgto}.csv"'

    # Cria o escritor CSV
    writer = csv.writer(response)

    # Escreve o cabeçalho do CSV
    writer.writerow([
        'Número', 'Ano', 'Processo', 'Fiscal', 'Valor Total', 'Descrição', 'Data de Emissão', 'Data de Conclusão'
    ])

    # Escreve os dados das ordens no CSV
    for ordem in ordens_concluidas:
        # Formata o valor total com duas casas decimais
        valor_total_formatado = f"{ordem['valor_total'] or 0:.2f}".replace('.', ',')

        writer.writerow([
            ordem['numero'],
            ordem['ano'],
            ordem['processo'],
            ordem['fiscal__nome_fiscal'],
            valor_total_formatado,  # Valor total formatado
            ordem['descricao'],
            ordem['data_emissao'].strftime('%d/%m/%Y') if ordem['data_emissao'] else '',  # Formata a data
            ordem['data_conclusao'].strftime('%d/%m/%Y') if ordem['data_conclusao'] else '',  # Formata a data
        ])

    return response

@login_required
def listar_meses_pagamento(request):
    # Obtém todos os meses de pagamento
    meses_pagamento = MesPagamento.objects.all()

    context = {
        'meses_pagamento': meses_pagamento,
    }

    return render(request, 'dserv/listar_meses_pagamento.html', context)

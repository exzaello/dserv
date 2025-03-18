import os
import django
from datetime import datetime

# Configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_ufac.settings')
django.setup()

from dserv.models import OrdemDeServico, Fiscal, Categoria, Situacao, MesPagamento

# Dados das ordens de serviço
ordens = [
    {
        "numero": 152,
        "ano": 2025,
        "processo": "23107.004442/2025-07",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 19),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção dos dispensers."
    },
    {
        "numero": 153,
        "ano": 2025,
        "processo": "23107.005222/2025-92",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 19),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção das portas do refeitório do térreo do RU, pois o limitador não está funcionando."
    },
    {
        "numero": 155,
        "ano": 2025,
        "processo": "23107.002382/2025-80",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 19),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção fluxo de água que vem da sala de máquinas do ar-condicionado central."
    },
    {
        "numero": 156,
        "ano": 2025,
        "processo": "23107.003039/2025-52",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 19),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo no teto do saguão."
    },
    {
        "numero": 157,
        "ano": 2025,
        "processo": "23107.005463/2025-31",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 19),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Identificação dos extintores, instalação da mangueira na caixa, correção das placas com identificação errada dos extintores."
    },
    {
        "numero": 159,
        "ano": 2025,
        "processo": "23107.028339/2024-63",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 20),
        "data_conclusao": None,
        "fiscal": "Lisângela Pazinatto",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção das réguas e rodapés em madeira danificadas."
    },
    {
        "numero": 160,
        "ano": 2025,
        "processo": "23107.027268/2024-81",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 20),
        "data_conclusao": None,
        "fiscal": "Lisângela Pazinatto",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da rampa de acesso do estacionamento, instalação de piso podotátil em concreto na rampa, e pintura."
    },
    {
        "numero": 161,
        "ano": 2025,
        "processo": "23107.006067/2025-21",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 20),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Fechadura."
    },
    {
        "numero": 162,
        "ano": 2025,
        "processo": "23107.006180/2025-15",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 21),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da janela do banheiro masculino."
    },
    {
        "numero": 163,
        "ano": 2025,
        "processo": "23107.006183/2025-41",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 21),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção no telhado."
    },
    {
        "numero": 164,
        "ano": 2025,
        "processo": "23107.006235/2025-89",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 21),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca do miolo de fechadura."
    },
    {
        "numero": 165,
        "ano": 2025,
        "processo": "23107.005988/2025-77",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 22),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção do sistema hidráulico."
    },
    {
        "numero": 168,
        "ano": 2025,
        "processo": "23107.004321/2025-57",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 22),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo nas torneiras do banheiro masculino."
    },
    {
        "numero": 169,
        "ano": 2025,
        "processo": "23107.006059/2025-85",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 22),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção ralos."
    },
    {
        "numero": 170,
        "ano": 2025,
        "processo": "23107.006042/2025-28",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 22),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da cerca de arame ao lado do portão de acesso."
    },
    {
        "numero": 171,
        "ano": 2025,
        "processo": "23107.006265/2025-95",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 22),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo do telhado."
    },
    {
        "numero": 172,
        "ano": 2025,
        "processo": "23107.006318/2025-78",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 24),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção na parte hidráulica da tubulação."
    },
    {
        "numero": 173,
        "ano": 2025,
        "processo": "23107.006378/2025-91",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 24),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da cobertura do laboratório."
    },
    {
        "numero": 174,
        "ano": 2025,
        "processo": "23107.006362/2025-88",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 24),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção do sistema hidráulico."
    },
    {
        "numero": 175,
        "ano": 2025,
        "processo": "23107.006356/2025-21",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 25),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção no teto do prédio."
    },
    {
        "numero": 176,
        "ano": 2025,
        "processo": "23107.006444/2025-22",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 25),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção na cobertura."
    },
    {
        "numero": 177,
        "ano": 2025,
        "processo": "23107.006363/2025-22",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 25),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da faixas antiderrapante da rampa que dá acesso ao anexo da BC."
    },
    {
        "numero": 178,
        "ano": 2025,
        "processo": "23107.006491/2025-76",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 25),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Ralo está sem tampa."
    },
    {
        "numero": 180,
        "ano": 2025,
        "processo": "23107.006548/2025-37",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção a Torneira da entrada do RU."
    },
    {
        "numero": 181,
        "ano": 2025,
        "processo": "23107.006588/2025-89",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo na mangueira de água da torneira."
    },
    {
        "numero": 182,
        "ano": 2025,
        "processo": "23107.006508/2025-95",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção no vaso sanitário."
    },
    {
        "numero": 183,
        "ano": 2025,
        "processo": "23107.006538/2025-00",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca da fechadura."
    },
    {
        "numero": 184,
        "ano": 2025,
        "processo": "23107.006617/2025-11",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Problema hidráulico."
    },
    {
        "numero": 185,
        "ano": 2025,
        "processo": "23107.006638/2025-28",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca do registro do chuveiro."
    },
    {
        "numero": 187,
        "ano": 2025,
        "processo": "23107.006607/2025-77",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 26),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca da fechadura."
    },
    {
        "numero": 189,
        "ano": 2025,
        "processo": "23107.024316/2024-80",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 28),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca de parte do piso."
    },
]

# Inserção dos dados no banco de dados
for ordem in ordens:
    fiscal, _ = Fiscal.objects.get_or_create(nome_fiscal=ordem['fiscal'])
    categoria, _ = Categoria.objects.get_or_create(categoria=ordem['categoria'])
    situacao, _ = Situacao.objects.get_or_create(situacao=ordem['situacao'])
    mespgto, _ = MesPagamento.objects.get_or_create(mes_pgto=ordem['mespgto'])
    
    OrdemDeServico.objects.create(
        numero=ordem['numero'],
        ano=ordem['ano'],
        processo=ordem['processo'],
        prazo=ordem['prazo'],
        data_emissao=ordem['data_emissao'],
        data_conclusao=ordem['data_conclusao'],
        fiscal=fiscal,
        categoria=categoria,
        situacao=situacao,
        mespgto=mespgto,
        descricao=ordem['descricao']
    )

print("Dados inseridos com sucesso!")

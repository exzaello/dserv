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
        "numero": 51,
        "ano": 2025,
        "processo": "23107.000289/2025-31",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção da pia da sala de indução que está entupida."
    },
    {
        "numero": 52,
        "ano": 2025,
        "processo": "23107.000489/2025-93",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Registro do mictório do banheiro masculino do Laboratório de Anatomia."
    },
    {
        "numero": 53,
        "ano": 2025,
        "processo": "23107.000466/2025-89",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção nos banheiros, dos alunos, masculino e feminino."
    },
    {
        "numero": 54,
        "ano": 2025,
        "processo": "23107.032660/2024-42",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção no banheiro feminino da PROPEG, suporte de papel higiênico, troca de uma tampa do vaso que está quebrada, a troca de uma descarga que esta vazando água, bem como a reposição de um chuveiro comum."
    },
    {
        "numero": 56,
        "ano": 2025,
        "processo": "23107.003042/2025-76",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": datetime(2025, 2, 7),
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "CONCLUIDO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção na pia, pois o sifão está danificado, vazando água, e necessita de substituição."
    },
    {
        "numero": 57,
        "ano": 2025,
        "processo": "23107.000561/2025-82",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 29),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção do banheiro masculino do Nai, sifão da pia está quebrado."
    },
    {
        "numero": 58,
        "ano": 2025,
        "processo": "23107.003333/2025-64",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 30),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção emergencial na Sala 05, pois, devido à quebra de uma telha, a água da chuva entrou no ambiente."
    },
    {
        "numero": 63,
        "ano": 2025,
        "processo": "23107.003393/2025-87",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 30),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção nos banheiros."
    },
    {
        "numero": 64,
        "ano": 2025,
        "processo": "23107.002672/2025-23",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 30),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção nos banheiros do bloco dos Mestrado."
    },
    {
        "numero": 66,
        "ano": 2025,
        "processo": "23107.002616/2025-99",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 31),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção nos vasos sanitários do banheiro feminino do Restaurante Universitário, box 2 e 3, visto que as descargas não estão funcionando e mesmo assim fica vazando grande quantidade de água."
    },
    {
        "numero": 67,
        "ano": 2025,
        "processo": "23107.003414/2025-64",
        "prazo": 1,
        "data_emissao": datetime(2025, 1, 31),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Substituição da janela do Laboratório Multidisciplinar de Ciências do Esporte, uma vez que a mesma se encontra estilhaçada, representando risco iminente de ruptura."
    },
    {
        "numero": 69,
        "ano": 2025,
        "processo": "23107.033398/2025-53",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 3),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Forro em declínio."
    },
    {
        "numero": 70,
        "ano": 2025,
        "processo": "23107.033497/2025-35",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 3),
        "data_conclusao": None,
        "fiscal": "Gerson Figueiredo de Oliveira",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Fechmaneot de muro."
    },
    {
        "numero": 71,
        "ano": 2025,
        "processo": "23107.______/2025-__",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 5),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção, reparo e troca dos itens danificados nos banheiros masculinos e femininos."
    },
    {
        "numero": 79,
        "ano": 2025,
        "processo": "23107.028223/2024-24",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 5),
        "data_conclusao": None,
        "fiscal": "Paulo Roberto de Lima Mendes",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Vários."
    },
    {
        "numero": 83,
        "ano": 2025,
        "processo": "23107.003902/2025-71",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 5),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo nos dois sanitários."
    },
    {
        "numero": 84,
        "ano": 2025,
        "processo": "23107.032864/2024-83",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção numa Prancha/peça de madeira da passarela."
    },
    {
        "numero": 85,
        "ano": 2025,
        "processo": "23107.022597/2025-36",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Suportes de papel higiênico, toalha e sabonete."
    },
    {
        "numero": 86,
        "ano": 2025,
        "processo": "23107.017540/2025-34",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção em alguns pisos cerâmicos."
    },
    {
        "numero": 87,
        "ano": 2025,
        "processo": "23107.004071/2025-55",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção de três válvulas de descarga dos banheiros."
    },
    {
        "numero": 89,
        "ano": 2025,
        "processo": "23107.004135/2025-18",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "A substituição de 1 tampa de vaso sanitário, 1 Torneira para Pia, 4 porta papel toalha e 1 porta sabonete líquido."
    },
    {
        "numero": 90,
        "ano": 2025,
        "processo": "23107.004333/2025-81",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca/substituição das fechaduras."
    },
    {
        "numero": 91,
        "ano": 2025,
        "processo": "23107.004157/2025-88",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Instalação de dispensador de sabonete."
    },
    {
        "numero": 92,
        "ano": 2025,
        "processo": "23107.003048/2025-43",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Instalação de 4 suportes de papel toalha e a instalação de 4 suportes para sabão líquido."
    },
    {
        "numero": 93,
        "ano": 2025,
        "processo": "23107.004123/2025-93",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo de uma goteira."
    },
    {
        "numero": 94,
        "ano": 2025,
        "processo": "23107.003717/2025-87",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 6),
        "data_conclusao": datetime(2025, 2, 17),
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "CONCLUIDO",
        "mespgto": "fevereiro/2025",
        "descricao": "Desentupimento do Vaso Sanitario."
    },
    {
        "numero": 95,
        "ano": 2025,
        "processo": "23107.004317/2025-99",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 9),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo de descarga."
    },
    {
        "numero": 96,
        "ano": 2025,
        "processo": "23107.022790/2025-77",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 10),
        "data_conclusao": None,
        "fiscal": "Lisângela Pazinatto",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção e limpeza da calha de água pluvial; manutenção do forro de gesso."
    },
    {
        "numero": 98,
        "ano": 2025,
        "processo": "23107.002410/2025-88",
        "prazo": 30,
        "data_emissao": datetime(2025, 2, 10),
        "data_conclusao": None,
        "fiscal": "Paulo Roberto de Lima Mendes",
        "categoria": "ORDINARIA",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Reparo na pintura."
    },
    {
        "numero": 99,
        "ano": 2025,
        "processo": "23107.004330/2025-48",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 9),
        "data_conclusao": None,
        "fiscal": "Emerson Henrique Costa de Araújo",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Troca da fechadura."
    },
    {
        "numero": 100,
        "ano": 2025,
        "processo": "23107.003910/2025-18",
        "prazo": 1,
        "data_emissao": datetime(2025, 2, 9),
        "data_conclusao": None,
        "fiscal": "Edilberto Ferreira Jansen Júnior",
        "categoria": "EMERGENCIAL",
        "situacao": "EM ANDAMENTO",
        "mespgto": "fevereiro/2025",
        "descricao": "Manutenção do telhado."
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

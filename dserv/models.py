from django.db import models
from datetime import date

# Create your models here.

class Fiscal(models.Model):
    """Fiscal técnico contrato"""
    nome_fiscal = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Fiscais'
    
    def __str__(self):
        return self.nome_fiscal

class Categoria(models.Model):
    """Categoria da Ordem de Serviço"""
    categoria = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.categoria

class Situacao(models.Model):
    """Situação da Ordem de Serviço"""
    situacao = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'Situacao'
    
    def __str__(self):
        return self.situacao
        
class MesPagamento(models.Model):
    """Mês de pagamento da Ordem de Serviço"""
    mes_pgto = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'MesPagamento'
        
    def __str__(self):
        return self.mes_pgto

class Empenho(models.Model):
    """Empenhos do contrato"""
    numero_emp = models.CharField(max_length=12, primary_key=True)
    valor_emp = models.DecimalField(max_digits=11, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Empenhos'
    
    def __str__(self):
        return self.numero_emp

class Bloco(models.Model):
    """Bloco da Universidade"""
    nome_bloco = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = 'Blocos'
    
    def __str__(self):
        return self.nome_bloco
        
class OrdemDeServico(models.Model):
    """Dados da ordem de serviço a ser cadastrada"""
    #Define o ano atual para campo padrão
    ano_atual = int(date.today().year)
    
    numero = models.IntegerField()
    ano = models.IntegerField(default=ano_atual)
    processo = models.CharField(max_length=20)
    prazo = models.IntegerField()
    data_emissao = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    fiscal = models.ForeignKey(Fiscal, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    situacao = models.ForeignKey(Situacao, on_delete=models.PROTECT)
    mespgto = models.ForeignKey(MesPagamento, on_delete=models.PROTECT)
    descricao = models.TextField()
    empenhos = models.ManyToManyField(
        Empenho, through="EmpenhoUtilizado"
    )
    blocos = models.ManyToManyField(
        Bloco, through="ManutencaoBloco"
    )
    
    class Meta:
        #Define ordme/ano como únicos
        constraints = [
            models.UniqueConstraint(
                fields=["numero", "ano"], name="numero_ano"
            ),
        ]
        verbose_name_plural = 'OrdensDeServico'
        
        #Define as permissões
        permissions = [
            ("cadastrar_ordem", "Pode cadastrar nova ordem"),
            ("editar_ordem", "Pode editar uma ordem cadastrada"),
            ("exportar_relatorio", "Pode exportar relatório de pagamento"),
        ]
    
    def __str__(self):
        return str(self.numero) + "/" + str(self.ano)

class EmpenhoUtilizado(models.Model):
    """Registra o valor dos empenhos utilizados em uma O.S."""
    ordem = models.ForeignKey(
        OrdemDeServico, on_delete=models.CASCADE,
        related_name="empenhos_utilizados"
    )
    empenho = models.ForeignKey(Empenho, on_delete=models.CASCADE)
    valor_utilizado = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'EmpenhoUtilizado'
        
    def __str__(self):
        return str(self.ordem) + " - " + str(self.empenho)
    
class ManutencaoBloco(models.Model):
    """Registra o valor gasto em cada bloco de uma ordem de serviço"""
    ordem = models.ForeignKey(
        OrdemDeServico, on_delete=models.CASCADE,
        related_name="valor_por_bloco"
    )
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    valor_bloco = models.DecimalField(max_digits=8, decimal_places=2)
    ambiente = models.CharField(max_length=400)
    
    class Meta:
        verbose_name_plural = 'ManutencaoBloco'
    
    def __str__(self):
        return str(self.ordem) + " - " + str(self.bloco)





from rest_framework import serializers

class SimularEtapa1Serializer(serializers.Serializer):
    # Campos obrigatórios - Thiago
    cpf = serializers.CharField(max_length=11, min_length=11)
    data_nascimento = serializers.CharField(max_length=10)
    login_certificado = serializers.CharField()
    codigo_tabela = serializers.IntegerField()
    prazo = serializers.IntegerField()
    valor_operacao = serializers.FloatField()
    valor_parcela = serializers.FloatField()
    coeficiente = serializers.FloatField()
    
    # Campos opcionais - Thiago
    vendedor = serializers.CharField(required=False, allow_blank=True)
    codigo_master = serializers.IntegerField(required=False)
    gerente_comercial = serializers.IntegerField(required=False)


class CadastrarDadosPessoaisSerializer(serializers.Serializer):
    # Campos obrigatórios para a  Etapa 2 - Thiago
    id_simulador = serializers.IntegerField() # PDF da Facta ta pedindp int 
    cpf = serializers.CharField(max_length=11, min_length=11) 
    nome = serializers.CharField()
    sexo = serializers.CharField(max_length=1)
    estado_civil = serializers.IntegerField()
    data_nascimento = serializers.CharField(max_length=10)
    rg = serializers.CharField()
    estado_rg = serializers.CharField(max_length=2)
    orgao_emissor = serializers.CharField()
    data_expedicao = serializers.CharField(max_length=10)
    estado_natural = serializers.CharField(max_length=2)
    cidade_natural = serializers.IntegerField()
    nacionalidade = serializers.IntegerField()
    celular = serializers.CharField()
    renda = serializers.IntegerField() # PDF da Factapede int 
    cep = serializers.CharField()
    endereco = serializers.CharField()
    numero = serializers.IntegerField()
    bairro = serializers.CharField()
    cidade = serializers.IntegerField()
    estado = serializers.CharField(max_length=2)
    nome_mae = serializers.CharField()
    nome_pai = serializers.CharField()
    valor_patrimonio = serializers.IntegerField()
    cliente_iletrado_impossibilitado = serializers.CharField(max_length=1)
    tipo_conta = serializers.CharField(max_length=1)
    banco = serializers.IntegerField()
    agencia = serializers.IntegerField()
    conta = serializers.CharField()
    matricula = serializers.CharField() # Mantido char pois PDF dá exemplo de ABC123 - Thiago
    cnpj_empregador = serializers.CharField()
    data_admissao = serializers.CharField(max_length=10)
    tipo_chave_pix = serializers.IntegerField() # PDF da facta pede SIM (obrigatori)
    chave_pix = serializers.CharField() # PDF da facta pede SIM  
    
    # opcionais ou condicionais -  Thiago
    pais_origem = serializers.IntegerField(required=False)
    complemento = serializers.CharField(required=False, allow_blank=True)
    banco_pagamento = serializers.IntegerField(required=False)
    agencia_pagamento = serializers.IntegerField(required=False)
    conta_pagamento = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    
    # Campos obrigatorios se o cliente for analfabeto == S - Thiago1
    nome_a_rogo = serializers.CharField(required=False, allow_blank=True)
    cpf_a_rogo = serializers.CharField(required=False, allow_blank=True)
    nome_a_rogo_testemunha = serializers.CharField(required=False, allow_blank=True)
    cpf_a_rogo_testemunha = serializers.CharField(required=False, allow_blank=True)


class GerarPropostaSerializer(serializers.Serializer):
    # Campos da Etapa 3 - Thiago
    codigo_cliente = serializers.IntegerField() 
    id_simulador = serializers.IntegerField() 
    tipo_formalizacao = serializers.CharField(required=False, default="DIG") # opcional 


class EnviarLinkFormalizacaoSerializer(serializers.Serializer):
    # Campos para o envio do link - Thiago 
    codigo_af = serializers.CharField() # id da proposta 
    tipo_envio = serializers.CharField() # pdf pede SIM (obrigatorio)

    #ARRUMAR OU RETIRAR OS COMENTARIOS ANTES DA ENTREGA (NAO ESQUECER)
from rest_framework import serializers

class SimularEtapa1Serializer(serializers.Serializer):
    # Campos obrigatórios 
    cpf = serializers.CharField(max_length=11, min_length=11)
    data_nascimento = serializers.CharField(max_length=10)
    login_certificado = serializers.CharField()
    codigo_tabela = serializers.IntegerField()
    prazo = serializers.IntegerField()
    valor_operacao = serializers.FloatField()
    valor_parcela = serializers.FloatField()
    coeficiente = serializers.FloatField()
    
    # Campos opcionais 
    vendedor = serializers.CharField(required=False, allow_blank=True)
    codigo_master = serializers.IntegerField(required=False)
    gerente_comercial = serializers.IntegerField(required=False)


class CadastrarDadosPessoaisSerializer(serializers.Serializer):
    # Campos obrigatórios da Etapa 2 
    id_simulador = serializers.IntegerField() # PDF pede int 
    cpf = serializers.CharField(max_length=11, min_length=11) # Mantido char para não perder zero à esquerda
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
    renda = serializers.IntegerField() # PDF pede int 
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
    matricula = serializers.CharField() # Mantido char pois PDF dá exemplo alfanumérico "ABC123" 
    cnpj_empregador = serializers.CharField()
    data_admissao = serializers.CharField(max_length=10)
    tipo_chave_pix = serializers.IntegerField() # PDF pede SIM (obrigatório) 
    chave_pix = serializers.CharField() # PDF pede SIM (obrigatório) 
    
    # Campos opcionais ou condicionais 
    pais_origem = serializers.IntegerField(required=False)
    complemento = serializers.CharField(required=False, allow_blank=True)
    banco_pagamento = serializers.IntegerField(required=False)
    agencia_pagamento = serializers.IntegerField(required=False)
    conta_pagamento = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    
    # Dados obrigatórios APENAS se cliente_iletrado_impossibilitado == "S" 
    nome_a_rogo = serializers.CharField(required=False, allow_blank=True)
    cpf_a_rogo = serializers.CharField(required=False, allow_blank=True)
    nome_a_rogo_testemunha = serializers.CharField(required=False, allow_blank=True)
    cpf_a_rogo_testemunha = serializers.CharField(required=False, allow_blank=True)


class GerarPropostaSerializer(serializers.Serializer):
    # Campos da Etapa 3 [cite: 479, 485, 488]
    codigo_cliente = serializers.IntegerField() # PDF pede int 
    id_simulador = serializers.IntegerField() # PDF pede int 
    tipo_formalizacao = serializers.CharField(required=False, default="DIG") # PRE ou DIG, opcional [cite: 485, 488, 489]


class EnviarLinkFormalizacaoSerializer(serializers.Serializer):
    # Campos do Envio de Link 
    codigo_af = serializers.CharField() # ID da proposta 
    tipo_envio = serializers.CharField() # PDF pede SIM (obrigatório)
# API Consignado - Backend (BFF)

Este projeto é um Backend for Frontend (BFF) construído em Django REST Framework. Ele atua como intermediário seguro entre a aplicação front-end (Vue.js) e as APIs parceiras de originação de crédito: **Facta Financeira** e **Nova Vida TI (NVCheck)**.

## 🚀 Pré-requisitos

Para rodar este projeto no computador da empresa (onde o IP está autorizado na whitelist das APIs), você precisará ter instalado:
* **Docker** e **Docker Compose** (O [Docker Desktop](https://www.docker.com/products/docker-desktop/) já inclui ambos no Windows/Mac).

Nenhum ambiente Python precisa ser configurado localmente na máquina hospedeira, pois tudo rodará de forma isolada dentro do container.

## ⚙️ Passo 1: Configuração das Variáveis de Ambiente

Por questões de segurança, senhas e chaves não estão no código-fonte. Você precisa criar o arquivo de configuração local na máquina da empresa.

1. Na raiz do projeto (mesma pasta deste README), crie um arquivo chamado exatamente `.env` (com o ponto no início).
2. Preencha o arquivo com as credenciais fornecidas pela empresa:

```env
# Configurações do Django
SECRET_KEY=cole-uma-chave-aleatoria-e-segura-aqui
DEBUG=True

# Credenciais da FACTA Financeira
FACTA_API_URL=[https://webservice.facta.com.br/](https://webservice.facta.com.br/)
FACTA_USUARIO=usuario_fornecido_pela_empresa
FACTA_SENHA=senha_fornecida_pela_empresa

# Credenciais da Nova Vida TI (Consulta NVCheck)
NOVA_VIDA_URL=[https://wsnv.novavidati.com.br/wslocalizador.asmx](https://wsnv.novavidati.com.br/wslocalizador.asmx)
NOVA_VIDA_USUARIO=usuario_fornecido
NOVA_VIDA_SENHA=senha_fornecida
NOVA_VIDA_CLIENTE=cliente_fornecido


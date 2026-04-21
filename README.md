# BFF - Integração de Crédito Consignado

Este projeto é um Backend for Frontend (BFF) construído com Django REST Framework. Ele atua como uma camada intermediária segura para consumir APIs de originação de crédito e consulta de dados, tratando autenticações, regras de negócio e validação de dados antes de enviá-los ao front-end (Vue.js).

## 🚀 Tecnologias Utilizadas
- Python 3.10
- Django & Django REST Framework
- Docker & Docker Compose
- Requests (com Connection Pooling e Timeouts)
- Cache Nativo (Gerenciamento de Tokens)

---

## ⚙️ Como rodar o projeto localmente (Ambiente da Empresa)

Siga o passo a passo abaixo para rodar o ambiente empacotado via Docker. Não é necessário instalar o Python na máquina, apenas o Docker.

### Passo 1: Clone o repositório e acesse a pasta
Abra o terminal no local onde deseja salvar o projeto e rode:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DA_PASTA_DO_PROJETO>


Passo 2: Configuração das Variáveis de Ambiente
Como o projeto é público, as senhas e URLs não estão no repositório.

Crie um arquivo chamado .env na raiz do projeto.

Solicite as chaves de acesso, usuários e URLs (APIs Facta e Nova Vida) aos responsáveis e preencha o arquivo .env.

Passo 3: Subir os Containers
Com o .env configurado, construa e suba a aplicação com o Docker Compose:
docker-compose up --build

(Dica: Se quiser que o terminal fique livre para uso, adicione a flag -d no final: docker-compose up -d --build)

O Docker fará a instalação das dependências, rodará as migrações automáticas do banco de dados e iniciará o servidor.

Passo 4: Acessar a Aplicação
Se tudo deu certo, o servidor estará rodando e escutando as requisições do front-end na porta 8000.

URL Base local: http://localhost:8000

Passo 5: Derrubar os Containers
Quando terminar o trabalho ou quiser desligar o servidor de forma segura, abra o terminal na pasta do projeto e rode:
docker-compose down

Principais Endpoints Disponíveis para o Front-end
Consultar Operações: GET /api/operacoes-disponiveis/

Simulação (Etapa 1): POST /api/simular-etapa1/

Cadastro (Etapa 2): POST /api/cadastrar-dados/

Proposta (Etapa 3): POST /api/gerar-proposta/

Envio de Link: POST /api/enviar-link/

Consulta de Dados (NVCheck): POST /api/consulta-nvcheck/

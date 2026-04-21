# 1. Usa a imagem oficial do Python, versão 3.10 (leve)
FROM python:3.10-slim

# 2. Impede que o Python grave arquivos .pyc e força o log a sair no terminal sem atraso
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Define a pasta de trabalho dentro do container
WORKDIR /app

# 4. Copia o arquivo de dependências primeiro (otimiza o cache do Docker)
COPY requirements.txt /app/

# 5. Instala as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Copia todo o resto do projeto para dentro da pasta /app no container
COPY . /app/

# 7. Expõe a porta 8000 que o Django vai usar
EXPOSE 8000

# 8. Comando para rodar o servidor quando o container ligar (escutando em todas as redes 0.0.0.0)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
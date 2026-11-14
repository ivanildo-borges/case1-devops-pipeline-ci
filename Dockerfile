# Usa uma imagem oficial mínima para reduzir a superfície de vulnerabilidades.
FROM python:3.12-alpine

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Atualiza os pacotes do Alpine para receber correções de segurança.
RUN apk upgrade --no-cache

# Define variáveis de ambiente para evitar a criação de arquivos .pyc 
# e para que o Python não faça buffering da saída
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copia apenas as dependências de runtime (otimização de cache do Docker)
COPY requirements.txt .

# Instala somente as dependências necessárias em produção.
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip uninstall -y pip setuptools

# Copia o resto do código da aplicação para dentro do contêiner
COPY . .

# Expõe a porta 5000 para o mundo exterior
EXPOSE 5000

# Executa com usuário sem privilégios.
RUN adduser -D -H -s /sbin/nologin appuser \
    && chown -R appuser:appuser /app
USER appuser

# Comando para rodar a aplicação quando o conteiner iniciar
CMD ["python", "main.py"]
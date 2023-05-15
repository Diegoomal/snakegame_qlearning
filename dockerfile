# Usa uma imagem do Python como base
FROM python:3.8-alpine

RUN pip install --upgrade pip
RUN pip install tk numpy

# Define o diretório de trabalho do contêiner
WORKDIR /src/game/

# Copia todo o conteúdo do diretório src/app para o diretório /app do contêiner
COPY src/game/ .

# Executa o comando padrão do contêiner (neste caso, executa o arquivo __init__.py)
CMD ["python", "main.py"]
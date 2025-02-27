FROM python:3.9-slim

# Definir diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos para o container
COPY requirements.txt requirements.txt
COPY src/ src/
COPY data/ data/

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Criar e configurar o arquivo config.toml do Streamlit
RUN mkdir -p ~/.streamlit && \
    echo "[server]" > ~/.streamlit/config.toml && \
    echo "runOnSave = true" >> ~/.streamlit/config.toml && \
    echo "headless = true" >> ~/.streamlit/config.toml && \
    echo "maxUploadSize = 200" >> ~/.streamlit/config.toml && \
    echo "serverAddress = '0.0.0.0'" >> ~/.streamlit/config.toml && \
    echo "serverPort = 8501" >> ~/.streamlit/config.toml

# Expor portas
EXPOSE 5000 8501

# Definir comando de inicialização
CMD ["sh", "-c", "python src/api/app.py & streamlit run src/streamlit/app.py --server.port=8501 --server.address=0.0.0.0"]

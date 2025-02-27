# Sistema de Recomendação de Notícias

## Estrutura do Projeto

O projeto segue a seguinte estrutura de diretórios:

```
/project-root
│── data/                     # Diretório com os datasets usados para treinamento e validação
│── models/
│   ├──recommender.pkl        # Modelo salvo após treinamento
│── src/
│   ├── train.py              # Script para treinar o modelo de recomendação
│   ├── predict.py            # Gera previsões a partir do modelo treinado
│   ├── utils.py              # Contém funções usadas em train.py e predict.py
│   ├── api/
│   │   ├── app.py            # Implementação do serviço REST com Flask
│   ├── streamlit/
│   │   ├── app.py            # Interface do usuário para visualizar as recomendações
│── requirements.txt          # Dependências do projeto
│── Dockerfile                # Configuração do container Docker
│── docker-compose.yml        # Orquestração dos serviços
│── README.md                 # Documentação do projeto
```

## Sequência de Processamento

1. **Treinamento do Modelo** (`train.py`)
   - Carrega os dados de histórico de usuários.
   - Processa e extrai features relevantes.
   - Treina um modelo de recomendação.
   - Salva o modelo para ser utilizado posteriormente.

2. **Geração de Previsões** (`predict.py`)
   - Carrega o modelo treinado.
   - Gera previsões para os usuários com base em seus históricos.
   - Salva as recomendações em um arquivo CSV.

3. **Serviço REST com Flask** (`api/app.py`)
   - Exibe recomendações ao receber requisições de um ID de usuário.
   - Faz consultas no modelo carregado.
   - Retorna os resultados no formato JSON.

4. **Interface do Streamlit** (`streamlit/app.py`)
   - Fornece uma interface gráfica onde o usuário pode inserir um ID e visualizar recomendações.
   - Chama a API Flask para obter recomendações.
   - Exibe os artigos recomendados de forma amigável.

## Execução do Projeto

Para rodar o projeto, siga estes passos:

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Treine o modelo
python src/train.py

# 3. Gere as previsões
python src/predict.py

# 4. Inicie a API Flask
python src/api/app.py

# 5. Rode a interface Streamlit
streamlit run src/streamlit/app.py
```

## Executando com Docker

```bash
# Construir imagens
docker-compose build

# Construir e rodar os containers
docker-compose up -d

# Parar os containers sem removê-los
docker-compose stop

# Para remover os containers e volumes
docker-compose down -v
```

## Testando

```markdown
### Testando a API Flask

A API pode ser testada utilizando `curl` ou ferramentas como Postman.

#### Exemplo de requisição:
```bash
curl -X GET http://localhost:5000/recommendations/3f3491a8fc9ed10caad74f95d22efcff9537bcaa631e6ab4278280fdc1e7b9ad
```
#### Exemplo de resposta:
```json
{
    "userId": "3f3491a8fc9ed10caad74f95d22efcff9537bcaa631e6ab4278280fdc1e7b9ad",
    "recommendations": [
        "news1",
        "news2",
        "news3"
    ]
}
```

### Testando no Streamlit

Após subir o Streamlit, acesse `http://localhost:8501` e insira um dos seguintes `userId` para testar:

- `e25fbee3a42d45a2914f9b061df3386b2ded2d8cc1f3d4b901419051126488b9`
- `3f3491a8fc9ed10caad74f95d22efcff9537bcaa631e6ab4278280fdc1e7b9ad`
- `d0afad7ea843d86597d822f0df1d39d31a3fea7c39fdeee870d49b897e1e99cd`
- `755062dd39a48809880cf363b04268c3af2c003088cde02636fcca973a3564d1`
- `ec1639851d99586c7f4da928deb49187303aec6e3b8d66c0359d4920e3c105e6`
- `0adffd7450d3b9840d8c6215f0569ad942e782fb19b805367b02b709b73f42a1`
- `a725fdc9d2db299299eac57ba5e9dc13ecee321ef4b9306cbfffea0cb3f837b8`

# Globo News Recommender

Este projeto tem como objetivo desenvolver um sistema de recomendação de notícias para a Globo utilizando modelos de aprendizado de máquina e técnicas de recomendação.

## Estrutura do Projeto
- **data/**: Contém os datasets de treino e validação.
- **notebooks/**: Análises exploratórias e desenvolvimento inicial dos modelos.
- **models/**: Modelos treinados salvos para uso na API.
- **src/**: Código-fonte principal do projeto.
  - **preprocessing/**: Scripts para limpeza e transformação dos dados.
  - **recommendation/**: Implementação dos modelos de recomendação.
  - **api/**: Serviço Flask para exposição das recomendações.
  - **streamlit/**: Interface para exibição das recomendações.
  - `train.py`: Script de treinamento do modelo.
  - `predict.py`: Script para gerar previsões a partir do modelo.
  - `utils.py`: Funções auxiliares.
- **Dockerfile**: Configuração para empacotamento com Docker.
- **docker-compose.yml**: Orquestração de serviços (API e Streamlit).
- **requirements.txt**: Dependências do projeto.

## Como Rodar o Projeto
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o treinamento do modelo:
   ```bash
   python src/train.py
   ```
3. Gerar previsões:
   ```bash
   python src/predict.py
   ```
4. Iniciar a API Flask:
   ```bash
   python src/api/app.py
   ```
5. Rode a interface Streamlit:
   ```bash
   streamlit run src/streamlit/app.py
   ```

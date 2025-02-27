import sys
import os
import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Caminhos dos arquivos
PREDICTIONS_FILE = "data/predictions.csv"
ITEMS_FILES = ["data/itens-parte1.csv", "data/itens-parte2.csv", "data/itens-parte3.csv"]

# Função para carregar os títulos das notícias
@st.cache_data
def load_news_items():
    news_df = pd.concat([pd.read_csv(f) for f in ITEMS_FILES])  # Carrega e junta os arquivos
    return news_df.set_index("page")  # Define "page" como índice para busca rápida

# Função para carregar as recomendações
@st.cache_data
def load_predictions():
    pred_df = pd.read_csv(PREDICTIONS_FILE)
    pred_df["recommendations"] = pred_df["recommendations"].apply(eval)  # Converte string para lista
    return pred_df.set_index("userId")

# Carregar dados
news_data = load_news_items()
predictions = load_predictions()

# Interface Streamlit
st.title("🔍 Recomendação de Notícias")

# Entrada do usuário
user_id = st.text_input("Digite um ID de usuário:", "")

if st.button("Obter Recomendações"):
    if user_id.strip() == "":
        st.warning("⚠️ Por favor, insira um ID de usuário.")
    elif user_id in predictions.index:
        recommended_news = predictions.loc[user_id, "recommendations"]

        st.subheader("📢 Notícias Recomendadas:")
        for news_id in recommended_news:
            if news_id in news_data.index:
                title = news_data.loc[news_id, "title"]
                url = news_data.loc[news_id, "url"]
                st.markdown(f"🔹 **[{title}]({url})**")
            else:
                st.markdown(f"⚠️ Notícia não encontrada: `{news_id}`")
    else:
        st.warning("⚠️ Nenhuma recomendação encontrada para este usuário.")

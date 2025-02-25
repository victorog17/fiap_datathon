import streamlit as st
import requests

st.title("Recomendação de Notícias")
user_id = st.text_input("Digite o ID do Usuário:")
if st.button("Obter Recomendações"):
    response = requests.get(f"http://localhost:5000/recommendations?userId={user_id}")
    st.write(response.json())

import streamlit as st
import pandas as pd

st.title('Lista de drinks')

# Leitura dos dados
url = "https://raw.githubusercontent.com/VitorB0/Drinks/refs/heads/main/dados1.csv"
dados = pd.read_csv(url, sep=";")

# Lista de ingredientes
ingredientes = [
    "Todos", "rum", "vodka", "cachaça", "triple sec", "coca", "limão", "cranberry",
    "hortelã", "água com gás", "vinho", "gin", "tônica", "fernet", "laranja",
    "cynar", "espuma de gengibre", "chá mate", "guaraná antartica"  
]

# Filtro
selected_ingredientes = st.multiselect(
    'Escolha os ingredientes do seu drink:', 
    ingredientes
)

st.write("Ingredientes selecionados:", selected_ingredientes)

# Aplica o filtro
if not selected_ingredientes:
    dados_filtrados = dados
else:
    dados_filtrados = dados
    for ingrediente in selected_ingredientes:
        dados_filtrados = dados_filtrados[dados_filtrados['Ingredientes'].str.contains(ingrediente, case=False, na=False)]

# Quebra de linha na coluna Ingredientes
dados_filtrados = dados_filtrados.copy()
dados_filtrados['Ingredientes'] = dados_filtrados['Ingredientes'].str.replace(r", \s*", ",<br>", regex=True)

# Estilos e renderização HTML
st.markdown("""
<style>
th {
    text-align: left !important;
    padding-left: 8px;
}
td:nth-child(2), th:nth-child(2) {
    white-space: pre-wrap;
    word-break: break-word;
    vertical-align: top;
    min-width: 200px;
    max-width: 200px;
    text-align: left;
}
table {
    width: 100%;
    border-collapse: collapse;
}
td, th {
    padding: 8px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

# Converte para HTML e exibe
st.markdown(dados_filtrados.to_html(escape=False, index=False), unsafe_allow_html=True)

import streamlit as st
import pandas as pd 


st.title('Lista de drinks')


# Leitura dos dados
url = "https://raw.githubusercontent.com/VitorB0/Drinks/refs/heads/main/dados1.csv"
dados = pd.read_csv(url, sep=";")


# Aplica quebra de linha apenas na coluna Ingredientes
dados['Ingredientes'] = dados['Ingredientes'].str.replace(', ', ',<br>', regex=False)
# Lista única dos ingredientes

ingredientes = [
    "Todos", "rum", "vodka", "cachaça", "triple sec", "coca", "limão", "cranberry",
     "hortelã", "água com gás", "vinho", "gin", "tônica", "fernet", "laranja",
    "cynar", "espuma de gengibre", "chá mate", "guaraná antartica"  
]



# Lista suspensa de ingredientes
selected_ingredientes = st.multiselect(
    'Escolha os ingredientes do seu drink:', 
    ingredientes,
)

# Listar os ingredientes selecionados
st.write("Ingredientes selecionados:", selected_ingredientes)

# Filtro de ingredientes na tabela principal
if len(selected_ingredientes) == 0:
    dados_filtrados = dados
else:
    dados_filtrados = dados
    for ingrediente in selected_ingredientes:
        dados_filtrados = dados_filtrados[dados_filtrados['Ingredientes'].str.contains(ingrediente, case=False, na=False)]


# Estilo para ajustar largura da coluna Ingredientes
st.markdown("""
<style>
th {
    text-align: left !important;
}
td:nth-child(2), th:nth-child(2) {
    white-space: pre-wrap;
    word-break: break-word;
    vertical-align: top;
    min-width: 200px;
    max-width: 200px;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# Exibe a tabela com HTML
st.markdown(dados.to_html(escape=False, index=False), unsafe_allow_html=True)



import streamlit as st
import pandas as pd 


st.title('Lista de drinks')


# Leitura dos dados
url = "https://raw.githubusercontent.com/VitorB0/Drinks/refs/heads/main/dados.csv"
dados = pd.read_csv(url, sep=";")



# Lista única dos ingredientes

ingredientes = [
    "Todos", "rum", "coca", "limão", "vodka", "triple sec", "suco de cranberry", "xarope de açúcar",
    "cachaça cravo e canela", "polpa de maracujá", "hortelã", "água com gás", "limão tahiti",
    "açúcar", "limão siciliano", "vinho", "gin", "tônica", "Fernet", "licor de limão",
    "clara de ovo", "Campari", "suco de laranja", "vermute tinto", "conhaque de gengibre",
    "Cynar", "laranja", "angostura"
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

# Listar os drinks filtrados
st.dataframe(dados_filtrados, use_container_width=True)

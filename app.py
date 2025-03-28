import streamlit as st
from streamlit_option_menu import option_menu

# Personalização do cabeçalho
st.set_page_config(page_title="Meu App", page_icon="🏠")
st.title("Meu App")  # Nome do aplicativo

# Mensagem de boas-vindas
st.write("Bem-vindo, Ataide!")

# Definir os botões principais (com ícones relacionados à função)
col1, col2 = st.columns([2, 2])

with col1:
    st.button("Domicílios", help="Cadastro de Domicílios", key="domicilios", use_container_width=True)

with col2:
    st.button("Famílias", help="Cadastro de Famílias", key="familias", use_container_width=True)

col1, col2 = st.columns([2, 2])

with col1:
    st.button("Cidadãos", help="Cadastro de Cidadãos", key="cidadaos", use_container_width=True)

with col2:
    st.button("Relatórios", help="Visualização de Relatórios", key="relatorios", use_container_width=True)

col1, col2 = st.columns([2, 2])

with col1:
    st.button("Resumo de Produção", help="Resumo de Produção", key="resumo_producao", use_container_width=True)

with col2:
    st.button("Nascimentos e Óbitos", help="Dados de Nascimentos e Óbitos", key="nascimentos_obitos", use_container_width=True)

col1, col2 = st.columns([2, 2])

with col1:
    st.button("Cartões Espelho", help="Visualizar Cartões Espelho", key="cartoes_espelho", use_container_width=True)

with col2:
    st.button("Laudos e Receitas", help="Gerenciar Laudos e Receitas", key="laudos_receitas", use_container_width=True)

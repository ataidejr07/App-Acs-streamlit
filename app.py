import streamlit as st  
from streamlit_option_menu import option_menu  

# Configuração da página  
st.set_page_config(page_title="Meu App", page_icon="🏠", layout="wide")  
st.title("Meu App")  # Nome do aplicativo  
st.write("Bem-vindo, Ataide!")  

# Sidebar para opções secundárias  
with st.sidebar:  
    st.header("Outras Opções")  
    st.button("Cartões Espelho", help="Visualizar Cartões Espelho", key="cartoes_espelho")  
    st.button("Laudos e Receitas", help="Gerenciar Laudos e Receitas", key="laudos_receitas")  

# Organização dos botões principais em seções  
st.subheader("Cadastros")  
col1, col2, col3 = st.columns(3)  
with col1:  
    st.button("Domicílios", help="Cadastro de Domicílios", key="domicilios", use_container_width=True)  
with col2:  
    st.button("Famílias", help="Cadastro de Famílias", key="familias", use_container_width=True)  
with col3:  
    st.button("Cidadãos", help="Cadastro de Cidadãos", key="cidadaos", use_container_width=True)  

st.subheader("Análises e Relatórios")  
col1, col2, col3 = st.columns(3)  
with col1:  
    st.button("Relatórios", help="Visualização de Relatórios", key="relatorios", use_container_width=True)  
with col2:  
    st.button("Resumo de Produção", help="Resumo de Produção", key="resumo_producao", use_container_width=True)  
with col3:  
    st.button("Nascimentos e Óbitos", help="Dados de Nascimentos e Óbitos", key="nascimentos_obitos", use_container_width=True)  

# Melhor espaçamento e uso do layout wide  
st.write("\n")

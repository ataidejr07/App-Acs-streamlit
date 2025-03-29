import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página

st.set_page_config(page_title="Meu App",
                   page_icon="🏠", layout="wide")
st.title("Meu App")  # Nome do aplicativo
st.write("Bem-vindo, Ataide!")

# Estilização dos botões como cartões clicáveis

st.markdown(""" <style> .card { padding: 15px; background-color: #f8f9fa; border-radius: 10px; border: 1px solid #ddd; text-align: center; cursor: pointer; font-size: 18px; font-weight: bold; margin-bottom: 10px; } .card:hover { background-color: #e9ecef; } </style> """, unsafe_allow_html=True)

# Sidebar para opções secundárias

with st.sidebar:
    st.header("Outras Opções")
    
    # Cartão "Cartões Espelho"
    if st.markdown('<div class="card">📋 Cartões Espelho</div>', unsafe_allow_html=True):
        st.write("Acessando Cartões Espelho")
    
    # Cartão "Laudos e Receitas"
    if st.markdown('<div class="card">📝 Laudos e Receitas</div>', unsafe_allow_html=True):
        st.write("Acessando Laudos e Receitas")

# Organização dos botões principais em seções

st.subheader("Cadastros") col1, col2, col3 = st.columns(3) with col1: if st.markdown('<div class="card">🏠 Domicílios</div>', unsafe_allow_html=True): st.write("Acessando Domicílios") with col2: if st.markdown('<div class="card">👨‍👩‍👧 Famílias</div>', unsafe_allow_html=True): st.write("Acessando Famílias") with col3: if st.markdown('<div class="card">🧑 Cidadãos</div>', unsafe_allow_html=True): st.write("Acessando Cidadãos")

st.subheader("Análises e Relatórios") col1, col2, col3 = st.columns(3) with col1: if st.markdown('<div class="card">📊 Relatórios</div>', unsafe_allow_html=True): st.write("Acessando Relatórios") with col2: if st.markdown('<div class="card">📈 Resumo de Produção</div>', unsafe_allow_html=True): st.write("Acessando Resumo de Produção") with col3: if st.markdown('<div class="card">👶⚰️ Nascimentos e Óbitos</div>', unsafe_allow_html=True): st.write("Acessando Nascimentos e Óbitos")


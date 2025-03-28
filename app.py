import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Meu App de Saúde", page_icon="🏥", layout="centered")

# Estilo personalizado
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .stButton>button {
        width: 100px;
        height: 100px;
        font-size: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .button-container {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        justify-content: center;
        align-items: center;
    }
    .title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout principal
st.markdown('<p class="title">Bem-vindo, Ataide!</p>', unsafe_allow_html=True)

# Container para os botões
col1, col2 = st.columns(2)

with col1:
    if st.button("📋 Pacientes", key="pacientes"):
        st.session_state.page = "pacientes"

    if st.button("📍 Endereços", key="enderecos"):
        st.session_state.page = "enderecos"

with col2:
    if st.button("📝 Visitas", key="visitas"):
        st.session_state.page = "visitas"

    if st.button("🔍 Filtrar", key="filtrar"):
        st.session_state.page = "filtrar"

# Gerenciamento de páginas
if "page" in st.session_state:
    if st.session_state.page == "pacientes":
        st.write("Página de Pacientes")
    elif st.session_state.page == "enderecos":
        st.write("Página de Endereços")
    elif st.session_state.page == "visitas":
        st.write("Página de Visitas")
    elif st.session_state.page == "filtrar":
        st.write("Página de Filtros")


import streamlit as st
from streamlit_extras.let_it_rain import rain

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", page_icon="🏥", layout="wide")

# Estilos customizados para o cabeçalho
st.markdown(
    """
    <style>
        .header {
            background-color: #007BFF;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            border-radius: 8px;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }
        .main-content {
            margin-top: 70px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Espaço para compensar o cabeçalho fixo
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Conteúdo principal
st.title("Bem-vindo, Ataíde!")

st.header("Cadastros")
st.button("🏠 Domicílios")
st.button("👨‍👩‍👧 Famílias")
st.button("🧑‍ Cidadãos")

st.header("Análises e Relatórios")
st.button("📊 Relatórios")

# Rodapé fixo
st.markdown(
    """
    <div style="position: fixed; bottom: 0; width: 100%; background-color: #007BFF; color: white; text-align: center; padding: 10px; border-radius: 8px;">
        Desenvolvido para ACS
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)

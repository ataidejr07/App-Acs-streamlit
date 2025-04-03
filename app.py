import streamlit as st

# Configuração da página
st.set_page_config(page_title="ACS Micro Área", layout="wide")

# Estilo CSS para o cabeçalho fixo
st.markdown(
    """
    <style>
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0A74DA;
            color: white;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            padding: 10px 0;
            z-index: 1000;
        }
        .main-content {
            margin-top: 60px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Espaço para compensar o cabeçalho fixo
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Menu lateral
with st.sidebar:
    st.title("Menu")
    if st.button("🏠 Domicílios (Lateral)"):
        st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")
    if st.button("📋 Cadastros (Lateral)"):
        st.info("Acesse os dados dos pacientes cadastrados.")
    if st.button("📄 Laudos e Receitas (Lateral)"):
        st.info("Consulte laudos e receitas médicas dos pacientes.")
    if st.button("🆔 Cartões Espelho (Lateral)"):
        st.info("Visualize cartões espelho dos pacientes.")

# Conteúdo principal
st.subheader("Bem-vindo, Ataide!")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Domicílios"):
        st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")
with col2:
    if st.button("📋 Cadastros"):
        st.info("Acesse os dados dos pacientes cadastrados.")
with col3:
    if st.button("📄 Laudos e Receitas"):
        st.info("Consulte laudos e receitas médicas dos pacientes.")

col4, col5 = st.columns(2)
with col4:
    if st.button("🆔 Cartões Espelho"):
        st.info("Visualize cartões espelho dos pacientes.")
with col5:
    if st.button("📊 Nascimentos e Óbitos"):
        st.info("Acompanhe registros de nascimentos e óbitos na sua área.")

# Fechando a div de conteúdo principal
st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

# Estilos personalizados para o cabeçalho e rodapé
st.markdown(
    """
    <style>
        .header {
            background-color: #007bff;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: white;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
        }
        .footer {
            background-color: #007bff;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: white;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
        }
        .main-content {
            padding-top: 60px;
            padding-bottom: 40px;
        }
        .welcome-text {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-bottom: -10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Cabeçalho fixo
st.markdown("<div class='header'>ACS Micro Área</div>", unsafe_allow_html=True)

# Conteúdo principal
st.markdown("<div class='main-content'>", unsafe_allow_html=True)
st.markdown("<p class='welcome-text'>Bem-vindo, Ataide!</p>", unsafe_allow_html=True)

st.subheader("Cadastros")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Domicílios"):
        st.info("Gerencie os endereços cadastrados e veja quem mora em cada residência.")
with col2:
    if st.button("👨‍👩‍👧‍👦 Famílias"):
        st.info("Visualize e edite os dados das famílias cadastradas.")
with col3:
    if st.button("🧑 Cidadãos"):
        st.info("Acesse informações detalhadas de cada cidadão.")

st.subheader("Análises e Relatórios")
col4, col5 = st.columns(2)

with col4:
    if st.button("📊 Relatórios"):
        st.info("Gere relatórios personalizados sobre os cadastros.")
with col5:
    if st.button("📈 Resumo de Produção"):
        st.info("Veja um resumo das visitas e atendimentos realizados.")

# Rodapé fixo
st.markdown("<div class='footer'>Desenvolvido para ACS | Versão 1.0</div>", unsafe_allow_html=True)

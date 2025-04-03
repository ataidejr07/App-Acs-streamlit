import streamlit as st

# Definir estilo CSS para cabeçalho azul e rodapé fixo
st.markdown(
    """
    <style>
    .header {
        background-color: #0A74DA;
        padding: 15px;
        text-align: center;
        font-size: 22px;
        color: white;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
    }
    .footer {
        background-color: #0A74DA;
        padding: 10px;
        text-align: center;
        font-size: 14px;
        color: white;
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
    }
    .content {
        padding-top: 60px;
        padding-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Criar menu lateral
st.sidebar.title("Menu")
st.sidebar.button("Laudos e Receitas")
st.sidebar.button("Cartões Espelho")
st.sidebar.button("Domicílios")
st.sidebar.button("Famílias")
st.sidebar.button("Cidadãos")
st.sidebar.button("Relatórios")
st.sidebar.button("Resumo de Produção")
st.sidebar.button("Nascimentos e Óbitos")

# Exibir conteúdo
st.markdown('<div class="content">', unsafe_allow_html=True)
st.title("Bem-vindo, Ataide!")
st.subheader("Cadastros")
st.button("🏠 Domicílios")
st.button("👨‍👩‍👦 Famílias")
st.button("🧑 Cidadãos")

st.subheader("Análises e Relatórios")
st.button("📊 Relatórios")
st.button("📈 Resumo de Produção")
st.button("👶⚰️ Nascimentos e Óbitos")
st.markdown('</div>', unsafe_allow_html=True)

# Exibir rodapé fixo
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)


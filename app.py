import streamlit as st

# Estilos globais para header e footer fixos
st.markdown("""
    <style>
        /* Cabeçalho fixo */
        .header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0052cc;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 20px;
            font-weight: bold;
            z-index: 1000;
        }

        /* Rodapé fixo */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0052cc;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            z-index: 1000;
        }

        /* Ajuste para não sobrepor conteúdo */
        .main-content {
            padding-top: 60px;
            padding-bottom: 40px;
        }

        /* Estilo dos botões */
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            border: 1px solid #ddd;
            padding: 8px;
            margin: 5px 0;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho fixo
st.markdown('<div class="header">ACS Micro Área</div>', unsafe_allow_html=True)

# Espaço para evitar sobreposição com o cabeçalho fixo
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Menu lateral
st.sidebar.title("Menu")
st.sidebar.button("🏠 Início")
st.sidebar.button("📄 Laudos e Receitas")
st.sidebar.button("🪪 Cartões Espelho")
st.sidebar.button("⚙ Configurações")

# Conteúdo principal
st.title("Bem-vindo, Ataide!")

st.subheader("Cadastros")
st.button("🏡 Domicílios")
st.button("👨‍👩‍👧 Famílias")
st.button("🧑 Cidadãos")

st.subheader("Análises e Relatórios")
st.button("📊 Relatórios")
st.button("📈 Resumo de Produção")
st.button("👶⚰ Nascimentos e Óbitos")

# Rodapé fixo
st.markdown('<div class="footer">Desenvolvido para ACS</div>', unsafe_allow_html=True)
